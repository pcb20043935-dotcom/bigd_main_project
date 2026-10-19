import pandas as pd
import matplotlib as plt

watchlist_df = pd.read_csv("watchlist.csv", dtype={"code": str})

print(watchlist_df["code"].tolist())
