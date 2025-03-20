from Bio import SeqIO


def remove_duplicates(input_file, output_file):
    sequence_dict = {}

    with open(input_file, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            sequence_name = record.id
            sequence = str(record.seq)

            if sequence_name not in sequence_dict:
                sequence_dict[sequence_name] = sequence
    with open(output_file, "w") as handle:
        for sequence_name, sequence in sequence_dict.items():
            handle.write(f">{sequence_name}\n{sequence}\n")


remove_duplicates(
    "ESP/data/our_data/our_data_add.fasta",
    "ESP/data/our_data/our_data_add_q.fasta",
)
