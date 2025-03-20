import subprocess
from io import StringIO

import torch
from Bio import SeqIO


def esmBuilding(inputfile, global_timestamp):
    outputdir = "data/cache/esm"
    esm_command = "python tools/extract.py esm1b_t33_650M_UR50S {} {} --repr_layers 33 --include mean --global_timestamp {}".format(
        inputfile, outputdir, global_timestamp
    )
    subprocess.call(esm_command, shell=True)
    try:
        output = subprocess.check_output(esm_command, shell=True)
        print("Command executed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
        print("Error output:")
        print(e)
        return "erro"


def readESM(dir: str):
    esm = torch.load(dir)
    esm_out = esm["mean_representations"][33].tolist()
    return esm_out
