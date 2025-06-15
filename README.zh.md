# Seq-P450：基于序列的深度学习模型预测P450酶底物催化
其他语言: [English Version](README.md)
# 目录
- [Seq-P450：基于序列的深度学习模型预测P450酶底物催化](#seq-p450基于序列的深度学习模型预测p450酶底物催化)
- [目录](#目录)
- [简介](#简介)
- [目录结构](#目录结构)
- [安装](#安装)
- [项目简介](#项目简介)
  - [CrossEvaluating](#crossevaluating)
  - [Seq-P450Training](#seq-p450training)
  - [Seq-P450ScreeningFourSpecies](#seq-p450screeningfourspecies)
# 简介
为提升 [ESP]([http](https://github.com/AlexanderKroll/ESP)) 模型对P450酶底物催化活性的预测性能，本研究通过整合已知的P450酶催化数据对模型进行了再训练。具体方法如下：首先，将已鉴定的P450酶及其对应底物构建为正样本集；其次，针对每个P450酶，从未被其催化的分子中随机选取两个小分子作为负样本。在特征工程方面，采用ESM1b模型提取蛋白质序列特征，并结合ECFP分子指纹技术对小分子进行编码。性能评估结果表明，经过优化的`Seq-P450`模型在预测准确性上较原始ESP模型有显著提升。我们还提供了在线预测服务：https://p450.biodesign.ac.cn/esp, 便于用户进行酶-底物催化关系的快速预测。

# 目录结构
```
.
├── data  --> 数据文件夹
│   ├── espData  --> esp数据
│   │   ├── encoded
│   │   └── model
│   ├── screeningData  --> 物种验证数据
│   │   ├── encoded
│   │   ├── enzyme
│   │   ├── esm
│   │   └── model
│   └── SeqP450Data  --> SeqP450数据
│       ├── encoded
│       ├── enzyme
│       ├── esm
│       ├── model
│       ├── output
│       ├── pair
│       └── substrate
└── src  --> 源代码
    ├── codes  --> 工具代码
    └── noteBooks  --> 开发代码
        ├── CrossEvaluating
        ├── Seq-P450ScreeningFourSpecies
        └── Seq-P450Training
```
# 安装
```bash
git clone https://github.com/JiangLab2020/Seq-P450.git
cd Seq-P450
conda env create -f environment.yml
```
# 项目简介
## CrossEvaluating
该模块通过五折交叉验证对模型的泛化性能进行评估。主要流程如下：
1. 数据预处理与划分
2. 基于训练集训练模型
3. 使用验证集进行Seq-P450性能评估
4. 使用验证集进行ESP性能评估
5. 对结果进行可视化分析
## Seq-P450Training
该模块引入新收集的P450酶-底物反应数据，重新训练模型。主要功能包括：
* 数据整合与特征提取
* 模型训练与参数保存
  
训练完成后可生成模型文件，用于后续预测任务。
## Seq-P450ScreeningFourSpecies
该模块通过在四个不同物种中进行反应筛选验证，进一步验证Seq-P450模型的跨物种预测能力。主要流程如下：
1. 数据整理与建模：构建物种特异性数据集，进行模型训练
2. 测试集构建：为每种酶构造候选底物集合
3. 反应预测：使用训练好的模型进行催化关系预测