import numpy as np


def create_input_and_output_data(df):
    X = ()
    y = ()
    for ind in df.index:
        emb = df["ESM1b"][ind]
        ecfp = np.array(list(df["ECFP"][ind])).astype(int)

        X = X + (np.concatenate([ecfp, emb]),)
        y = y + (df["Binding"][ind],)

    return (X, y)
