
# Seq-P450
# Contents
- [Seq-P450](#seq-p450)
- [Contents](#contents)
- [Introduction](#introduction)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
# Introduction
To improve the accuracy of the [ESP]([http](https://github.com/AlexanderKroll/ESP)) model in predicting substrate catalysis for P450 enzymes, we retrained it by integrating characterized P450 enzymes into the original training set. First, we designated P450 enzymes and their known catalyzed substrates as positive samples. For each enzyme, we randomly selected two small molecules—excluding its catalyzed substrates—as negative samples. Next, we encoded both positive and negative samples using the ESM1b model and ECFP molecular fingerprint technology. Comparative analysis between ESP and ESP-P450 revealed a significant improvement in prediction accuracy for Sequ-P450.\
We also offer web services here: https://p450.biodesign.ac.cn/esp
# Directory Structure
```
.
├── compare --> compare with other pipeline
│   ├── code  --> source code
│   ├── data  --> data
│   ├── ESPCalculate  --> source code
│   ├── input
│   ├── input_best
│   ├── input_new
│   ├── input_old
│   ├── others
│   ├── out4cj
│   ├── output
│   ├── substrateCalculate    --> source code
│   └── tools --> source code
├── data  --> Data warehouse
│   ├── author_data
│   ├── Mou_data
│   ├── our_data
│   ├── pu_epp
│   ├── splits
│   └── training_results
├── notebooks_and_code  --> ESP code
│   └── additional_code
├── our_codes --> develop code
└── Screening_and_application --> evaluate code
```
# Installation
```bash
git clone https://github.com/JiangLab2020/Sequ-P450.git
cd SequP450
conda env create -f environment.yml
```
