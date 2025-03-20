import numpy as np
import pandas as pd
import torch
import xgboost as xgb
from Bio import SeqIO
from rdkit import DataStructs
from substrateCalculate.getUploadData import getuserdata
from tools.toutf8 import convert_to_utf8

from ESPCalculate.calculateESM import esmBuilding, readESM
from ESPCalculate.ESP import create_input_and_output_data

adddef = False


def processing(whichDatabase, substratePath, enzymesPath, global_timestamp):
    # 1. esm and ecfp
    uploadECFP = getuserdata(substratePath)
    ecfp = DataStructs.BitVectToText(uploadECFP)
    data_list = []
    enzymesPath = convert_to_utf8(
        enzymesPath, f"data/cache/fasta/{enzymesPath.split('/')[-1]}_{global_timestamp}"
    )
    esmBuilding(enzymesPath, global_timestamp)
    with open(enzymesPath, "r", encoding="utf-8") as filefasta:
        proteins = SeqIO.parse(filefasta, "fasta")
        for p in proteins:
            esm = readESM(f"data/cache/esm/{p.id}_{global_timestamp}.pt")
            temp_dict = {
                "enzyme": p.id,
                "Sequence": p.seq,
                "ECFP": ecfp,
                "ESM1b": esm,
                "Binding": 1,
            }
            data_list.append(temp_dict)
    df_input = pd.DataFrame(data_list)
    data = {
        "ECFP": [ecfp],
    }
    df_substratedata = pd.DataFrame(data)
    df_enzymedata = pd.DataFrame(
        columns=["enzyme", "Sequence", "ECFP", "ESM1b", "Binding"]
    )
    # 2. read model and put data into model
    if whichDatabase == "P450":
        if adddef == True:
            df_enzymedata = pd.read_pickle("ESPCalculate/model/allP450enzyme.dat")
        bst = pd.read_pickle("ESPCalculate/model/p450normalmodel.pkl")
    elif whichDatabase == "UGT":
        if adddef == True:
            df_enzymedata = pd.read_pickle("ESPCalculate/model/allUGTenzyme.dat")
        bst = pd.read_pickle("ESPCalculate/model/ugtnormalmodel.pkl")
    elif whichDatabase == "author":
        bst = pd.read_pickle("ESPCalculate/model/p450authormodel.dat")
    else:
        raise Exception("unknown database")
    df_enzymedata["key"] = 1
    df_substratedata["key"] = 1
    result = pd.merge(df_enzymedata, df_substratedata, on="key", how="outer")
    result = result.dropna()
    result["ESM1b"] = None
    if whichDatabase == "P450":
        rep_dict = "data/enzyme/esm_p450/"
    elif whichDatabase == "UGT":
        rep_dict = "data/enzyme/esm_ugt/"
    elif whichDatabase == "author":
        rep_dict = "data/enzyme/esm_author/"
    else:
        raise Exception("unknown database")
        pass
    for ind in result.index:
        esms = torch.load(rep_dict + str(result["enzyme"][ind]) + ".pt")
        result.at[ind, "ESM1b"] = esms["mean_representations"][33].tolist()
    result["Binding"] = 0
    result.drop(columns="key", inplace=True)
    result = pd.concat([result, df_input], ignore_index=True)

    # 3. predict
    data_X, data_y = create_input_and_output_data(df=result)
    feature_names = ["ECFP_" + str(i) for i in range(1024)]
    feature_names = feature_names + ["ESM1b_" + str(i) for i in range(1280)]
    dwant = xgb.DMatrix(
        np.array(data_X), label=np.array(data_y), feature_names=feature_names
    )
    y_test_pred = bst.predict(dwant)
    result["scores"] = y_test_pred
    return result[["enzyme", "Sequence", "scores"]]
