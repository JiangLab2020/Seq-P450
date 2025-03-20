import argparse

from Bio import SeqIO

parser = argparse.ArgumentParser(description="")

parser.add_argument("--input", help="input file path")
parser.add_argument("--output", help="output file path")
args = parser.parse_args()


def remove_duplicates(input_file, output_file):
    sequence_dict = {}

    with open(input_file, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            sequence_name = record.id
            # sequence_name = record.id.split('_')[-1]
            sequence = str(record.seq).replace("*", "")

            if sequence_name not in sequence_dict:
                sequence_dict[sequence_name] = sequence
    with open(output_file, "w") as handle:
        for sequence_name, sequence in sequence_dict.items():
            handle.write(f">{sequence_name}\n{sequence}\n")


if __name__ == "__main__":
    input_path = args.input
    output_path = args.output
    remove_duplicates(input_path, output_path)
