# Seq-P450: A Sequence-Based Deep Learning Model for Predicting Substrate Catalysis of P450 Enzymes
Other languages: [中文版](README.zh.md)
# Contents
- [Seq-P450: A Sequence-Based Deep Learning Model for Predicting Substrate Catalysis of P450 Enzymes](#seq-p450-a-sequence-based-deep-learning-model-for-predicting-substrate-catalysis-of-p450-enzymes)
- [Contents](#contents)
- [Introduction](#introduction)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Project Overview](#project-overview)
  - [CrossEvaluating](#crossevaluating)
  - [Seq-P450Training](#seq-p450training)
  - [Seq-P450ScreeningFourSpecies](#seq-p450screeningfourspecies)
# Introduction
To improve the prediction performance of the [ESP]([http](https://github.com/AlexanderKroll/ESP)) model on the catalytic activity between P450 enzymes and their substrates, we retrained the model using integrated known catalytic data of P450 enzymes. The specific steps are as follows:
First, a positive sample set was constructed by pairing identified P450 enzymes with their known substrates.
Second, for each P450 enzyme, two small molecules that are not known to be catalyzed by the enzyme were randomly selected as negative samples.
For feature engineering, protein sequence representations were extracted using the ESM1b model, while small molecules were encoded using the ECFP molecular fingerprint method.
Performance evaluation showed that the optimized `Seq-P450` model achieved a significant improvement in prediction accuracy compared to the original ESP model.
An online prediction service is also provided for convenient enzyme-substrate catalytic relationship prediction:
https://p450.biodesign.ac.cn/esp

# Directory Structure
```
.
├── data  --> data folder
│   ├── espData  --> ESP data
│   │   ├── encoded
│   │   └── model
│   ├── screeningData  --> species validation data
│   │   ├── encoded
│   │   ├── enzyme
│   │   ├── esm
│   │   └── model
│   └── SeqP450Data  --> SeqP450 data
│       ├── encoded
│       ├── enzyme
│       ├── esm
│       ├── model
│       ├── output
│       ├── pair
│       └── substrate
└── src  --> source code
    ├── codes  --> utility code
    └── noteBooks  --> development code
        ├── CrossEvaluating
        ├── Seq-P450ScreeningFourSpecies
        └── Seq-P450Training
```

# Installation
```bash
git clone https://github.com/JiangLab2020/Seq-P450.git
cd Seq-P450
conda env create -f environment.yml
```


# Project Overview

## CrossEvaluating

This module evaluates the generalization performance of the model using five-fold cross-validation. The main workflow includes:

1. Data preprocessing and partitioning
2. Model training on the training set
3. Performance evaluation of Seq-P450 on the validation set
4. Performance evaluation of ESP on the validation set
5. Visualization and analysis of the results

## Seq-P450Training

This module incorporates newly collected P450 enzyme-substrate reaction data to retrain the model. The main functionalities include:

* Data integration and feature extraction
* Model training and parameter saving

Upon completion, the trained model file will be generated for downstream prediction tasks.

## Seq-P450ScreeningFourSpecies

This module evaluates the cross-species prediction capability of the Seq-P450 model by performing reaction screening and validation across four different species. The main workflow includes:

1. Data organization and modeling: construct species-specific datasets and perform model training
2. Test set construction: build candidate substrate sets for each enzyme
3. Reaction prediction: use the trained model to predict enzyme-substrate catalytic relationships
