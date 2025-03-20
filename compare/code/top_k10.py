def process(indataframe, queryname, topk, esp_partition):
    indataframe["score"] = (1 - esp_partition) * indataframe[
        "Gnina_score"
    ] + esp_partition * indataframe["ESP_p450_score"]
    cachedataframe = indataframe.sort_values("score", ascending=False)
    thresholds = indataframe["score"].quantile(1 - topk)
    cachedataframe[
        (cachedataframe["if_right"]) & (cachedataframe["Binding"] == 1)
    ].to_csv(
        f"../output/bin/test{queryname}.csv",
        header=False,
        index=False,
        mode="a",
    )
    return len(
        cachedataframe[
            (cachedataframe["if_right"])
            & (cachedataframe["Binding"] == 1)
            & (cachedataframe["score"] >= thresholds)
        ]
    ), len(
        cachedataframe[(cachedataframe["if_right"]) & (cachedataframe["Binding"] == 1)]
    )
