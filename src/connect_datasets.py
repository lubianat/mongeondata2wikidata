import pandas as pd
from pathlib import Path

HERE = Path(__file__).parent.resolve()
DATA = HERE.parent.joinpath("data").resolve()
RESULTS = HERE.parent.joinpath("results").resolve()

mongeon = pd.read_csv(DATA.joinpath("mongeon.csv"))
open_alex_wikidata = pd.read_csv(DATA.joinpath("open_alex_df.csv"))


mongeon["open_alex"] = [a.split("/")[-1] for a in mongeon["author_id"]]
merged_df = mongeon.merge(open_alex_wikidata, on="open_alex", how="inner")

merged_df.to_csv(RESULTS.joinpath("mongeon_to_wikidata.csv"))
