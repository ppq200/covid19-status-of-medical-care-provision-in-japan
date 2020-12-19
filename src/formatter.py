import pandas as pd


def get_formated_df(unformat_df):
    df = (
        unformat_df.iloc[9:57, 1:]
        .reset_index(drop=True)
        .rename(
            columns={
                "（参考）都道府県の医療提供体制等の状況（医療提供体制・監視体制・感染の状況）": "都道府県",
                # 単位: 千人
                "Unnamed: 2": "人口",
                #
                # 医療提供体制
                #
                # ステージ3の指標: 25%  ステージ4の指標: なし
                "Unnamed: 3": "確保_病床使用率",
                "Unnamed: 4": "確保_病床使用率_前週差",
                "Unnamed: 5": "確保想定_病床使用率",
                "Unnamed: 6": "確保想定_病床使用率_前週差",
                "Unnamed: 7": "確保_病床使用率_重症患者",
                "Unnamed: 8": "確保_病床使用率_重症患者_前週差",
                "Unnamed: 9": "確保想定_病床使用率_重症患者",
                "Unnamed: 10": "確保想定_病床使用率_重症患者_前週差",
                # 単位: 対人口10万人
                "Unnamed: 11": "療養者数",
                "Unnamed: 12": "療養者数_前週差",
                "Unnamed: 13": "調整列",
                #
                # 監視体制
                #
                "Unnamed: 14": "陽性者数_PCR検査件数_最近1週間",
                "Unnamed: 15": "陽性者数_PCR検査件数_最近1週間_前週差",
                "Unnamed: 16": "調整列_2",
                #
                # 感染の状況
                #
                "Unnamed: 17": "直近1週間の陽性者数",
                "Unnamed: 18": "直近1週間の陽性者数_前週差",
                "Unnamed: 19": "直近1週間とその前1週間の比",
                "Unnamed: 20": "直近1週間とその前1週間の比_前週差",
                "Unnamed: 21": "感染経路不明な者の割合",
                "Unnamed: 22": "感染経路不明な者の割合_前週差",
            }
        )
        .drop(columns=["調整列", "調整列_2"])
    )
    df["人口"] = df["人口"] * 1000
    return df


def get_point_of_time(unformat_df):
    df = (
        unformat_df.iloc[5:6, [2, 3, 5, 7, 9, 11, 14, 17, 21]]
        .reset_index(drop=True)
        .rename(
            columns={
                "Unnamed: 2": "人口_時点",
                "Unnamed: 3": "確保_病床使用率_時点",
                "Unnamed: 5": "確保想定_病床使用率_時点",
                "Unnamed: 7": "確保_病床使用率_重症患者_時点",
                "Unnamed: 9": "確保想定_病床使用率_重症患者_時点",
                "Unnamed: 11": "療養者数_時点",
                "Unnamed: 14": "陽性者数_PCR検査件数_最近1週間_時点",
                "Unnamed: 17": "直近1週間の陽性者数_時点",
                "Unnamed: 21": "感染経路不明な者の割合",
            }
        )
    )
    for col in (
        "確保_病床使用率_時点",
        "確保想定_病床使用率_時点",
        "確保_病床使用率_重症患者_時点",
        "確保想定_病床使用率_重症患者_時点",
        "療養者数_時点",
    ):
        df[col] = df[col].apply(lambda x: x.strftime("%Y-%m-%d"))
    return df


def get_annotations(unformat_df):
    annotaions = (
        unformat_df.iloc[58:, 1].dropna().values.tolist()
        + unformat_df.iloc[58:, 14].dropna().values.tolist()
    )
    table = str.maketrans({"\u3000": ""})
    annotations = list(dict.fromkeys([i.translate(table) for i in annotaions]))
    return pd.DataFrame(dict(annotation=annotations))


def get_indication(unformat_df):
    indication = (
        unformat_df.iloc[7:9, [1, 3, 5, 7, 9, 11, 14, 17, 19, 21]]
        .reset_index(drop=True)
        .rename(
            columns={
                "（参考）都道府県の医療提供体制等の状況（医療提供体制・監視体制・感染の状況）": "ステージ",
                "Unnamed: 3": "確保_病床使用率",
                "Unnamed: 5": "確保想定_病床使用率",
                "Unnamed: 7": "確保_病床使用率_重症患者",
                "Unnamed: 9": "確保想定_病床使用率_重症患者",
                "Unnamed: 11": "療養者数",
                "Unnamed: 14": "陽性者数_PCR検査件数_最近1週間",
                "Unnamed: 17": "直近1週間の陽性者数",
                "Unnamed: 19": "直近1週間とその前1週間の比",
                "Unnamed: 21": "感染経路不明な者の割合",
            }
        )
    ).fillna("-")
    return indication
