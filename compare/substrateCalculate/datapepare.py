import os

import pandas as pd
import pubchempy as pcp
from rdkit import Chem


def get_subname(sdfpath):
    try:
        suppl = Chem.SDMolSupplier(sdfpath)
        pubchem_cids = [
            mol.GetProp("PUBCHEM_COMPOUND_CID") for mol in suppl if mol is not None
        ]
        return pubchem_cids[0]
    except:
        return sdfpath


def id2name(cid):
    if cid.isalpha():
        return cid
    try:
        compound = pcp.Compound.from_cid(cid)
        synonyms = compound.synonyms
        compound_name = next((syn for syn in synonyms if syn), "Not Found")
        return compound_name
    except pcp.PubChemHTTPError:
        return cid


def sdfname2subname(inputpath, outputpath):
    pairs = {}
    for root, dirs, files in os.walk(inputpath):
        for file in files:
            if file.endswith(".sdf"):
                file_path = os.path.join(root, file)
                sdfname = file_path.split("/")[-1][:-4]
                pubnum = get_subname(file_path)
                subname = id2name(pubnum)
                pairs[sdfname] = [pubnum, subname]
    print(pairs)
    df = pd.DataFrame(pairs)
    df = df.T
    df.columns = ["pubnum", "subname"]
    df.to_csv(outputpath, header=None)


if __name__ == "__main__":
    # sdfname2subname('data/substrate/UGTSubstrate', 'data/pair/UGTpair.csv')
    sdfname2subname("data/substrate/P450Substrate", "data/pair/P450pair.csv")
