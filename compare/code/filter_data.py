import pandas as pd


def getcoldata(result, queryname):
    filtered_rows = result[(result["if_right"]) & (result["Binding"] == 1)]
    enzymes = filtered_rows["enzyme"].unique().tolist()
    substrates = [
        filtered_rows[(filtered_rows["enzyme"] == i) & (filtered_rows["Binding"] == 1)][
            "substrate"
        ].item()
        for i in enzymes
    ]
    dataframes = []
    combined_df = pd.DataFrame()
    for num, nowsubstrate in enumerate(substrates):
        resultcc = result[
            (
                result["cc"]
                == (
                    result[(result["enzyme"] == enzymes[num]) & (result["if_right"])][
                        "cc"
                    ].item()
                )
            )
            | (result["cc"].isnull())
        ]
        dataframes.append(resultcc[resultcc["substrate"] == nowsubstrate])
    for i, df in enumerate(dataframes):
        df = df.copy(deep=True)
        df.loc[:, "group"] = enzymes[i]
        combined_df = pd.concat([combined_df, df], ignore_index=True)
    combined_df.to_csv(f"../output/{queryname}.csv")
    grouped = combined_df.groupby("group")
    return grouped


def getsubdata(result, queryname):
    filtered_rows = result[(result["if_right"]) & (result["Binding"] == 1)]
    enzymes = filtered_rows["enzyme"].unique().tolist()
    substrates = [
        filtered_rows[(filtered_rows["enzyme"] == i) & (filtered_rows["Binding"] == 1)][
            "substrate"
        ].item()
        for i in enzymes
    ]

    dataframes = []
    combined_df = pd.DataFrame()
    for num, nowsubstrate in enumerate(substrates):
        resultcc = result[
            (
                result["cc"]
                == (
                    result[(result["enzyme"] == enzymes[num]) & (result["if_right"])][
                        "cc"
                    ].item()
                )
            )
            | (result["cc"].isnull())
        ]
        dataframes.append(resultcc[resultcc["substrate"] == nowsubstrate])
    for i, df in enumerate(dataframes):
        df = df.copy(deep=True)
        df.loc[:, "group"] = substrates[i]
        combined_df = pd.concat([combined_df, df], ignore_index=True)
    combined_df = combined_df.drop_duplicates()
    combined_df.to_csv(f"../output/{queryname}.csv", index=False)
    grouped = combined_df.groupby("group")
    return grouped
