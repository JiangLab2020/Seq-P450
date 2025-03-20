import sys

from rdkit import Chem
from rdkit.Chem import AllChem


def getuserdata(webinput):
    if webinput[-4:] == ".sdf":
        try:
            mol = Chem.MolFromMolFile(webinput)
            ecfp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=1024)
        except Exception as e:
            sys.stderr.write("eror: {}\n".format(e))
            sys.exit()
    elif webinput[0:5].lower() == "inchi":
        try:
            mol = Chem.MolFromInchi(webinput)
            ecfp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=1024)
        except Exception as e:
            sys.stderr.write("error: {}\n".format(e))
            sys.exit()
    else:
        try:
            mol = Chem.MolFromSmiles(webinput)
            ecfp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=1024)
        except Exception as e:
            sys.stderr.write("input error: {}\n".format(e))
            sys.exit()
    return ecfp
