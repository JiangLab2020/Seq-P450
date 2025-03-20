import os
import time

from ESPCalculate.processingESP import processing

global_timestamp = time.time()


# refername = "Arabidopsis_thaliana"
# refername = "Erigeron_breviscapus"
# refername = "Glycine_max"
# refername = "Zea_mays"
refername = "sheetall"

if __name__ == "__main__":
    with open(f"others/reme/{refername}reme.csv", "r") as f:
        times = 1
        for line in f:
            line = line.strip()
            index, substrate, smile = line.split(",")
            needsmile = smile.split(">>")[0]
            result = processing(
                "author", needsmile, f"others/reme/{refername}.fasta", global_timestamp
            )
            result.to_csv(f"data/output/esp/{refername}/{times}.csv", index=False)
            print(f"{refername} {times} finish")
            times += 1
    os.system("rm -rf data/cache/esm/*")
    os.system("rm -rf data/cache/fasta/*")
