import csv
import os
import sys

from Bio import SeqIO
from rdkit import Chem
from rdkit.Chem import AllChem, DataStructs


def process_sdf_file(folder_path):
    encoded_molecules = []
    sdf_files = [f for f in os.listdir(folder_path) if f.endswith(".sdf")]
    for sdf_file in sdf_files:
        file_path = os.path.join(folder_path, sdf_file)
        try:
            mol = Chem.MolFromMolFile(file_path)
            ecfp = AllChem.GetMorganFingerprintAsBitVect(mol, 2)
            encoded_molecules.append([sdf_file[:-4], ecfp])
        except Exception as e:
            print(str(e))
    return encoded_molecules


def loadData(Database):
    if Database == "UGT":
        encoded = process_sdf_file("data/substrate/UGTSubstrate")
    elif Database == "P450":
        encoded = process_sdf_file("data/substrate/P450Substrate")
    else:
        sys.stderr.write("error\n")
        sys.exit()
    return encoded


def calculationData(theDataBase: list, theUserData: str) -> dict:
    theCodedData = loadData(theDataBase)
    similarity_scores = {}
    for oneencoded in theCodedData:
        score = DataStructs.TanimotoSimilarity(theUserData, oneencoded[1])
        similarity_scores[oneencoded[0]] = score
    sorted_scores = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)[
        :10
    ]
    return sorted_scores


def get_fasta(database, fastaname):
    sequences = SeqIO.to_dict(
        SeqIO.parse(f"data/enzyme/{database}_enzyme_q.fasta", "fasta")
    )
    if fastaname in sequences:
        return sequences[fastaname].seq
    else:
        return ""


def sdf2smile(path):
    mols = Chem.SDMolSupplier(path)
    for mol in mols:
        smiles = Chem.MolToSmiles(mol)
        return smiles


def topair(pairdir):
    with open(pairdir, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        your_dict = {}
        for row in csvreader:
            key = row[0]
            values = [value for value in row[1:]]
            your_dict[key] = values
    return your_dict


def Process(sorted_scores, whichDatabase, pairdir, outputdir):
    pairdic = topair(pairdir)
    with open(outputdir, "w") as file:
        for name, scores in sorted_scores:
            pubid = pairdic[name][0]
            subname = pairdic[name][1]
            fastaseq = get_fasta(whichDatabase, name)
            file.write(f"{subname}\t{pubid}\t{scores}\t{name}\t{fastaseq}\n")
