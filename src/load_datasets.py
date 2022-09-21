import sys
import subprocess
from wikidata2df import wikidata2df
from pathlib import Path

HERE = Path(__file__).parent.resolve()
DATA = HERE.parent.joinpath("data").resolve()
RESULTS = HERE.parent.joinpath("results").resolve()

URL = (
    "https://zenodo.org/record/7013518/files/authors_tweeters_2022_08_21.csv?download=1"
)
subprocess.run(["wget", "-O", "data/mongeon.csv", "-nc", URL])

open_alex_query = HERE.joinpath("queries").joinpath("open_alex.rq").read_text()
open_alex_df = wikidata2df(open_alex_query)

open_alex_df.to_csv("data/open_alex_df.csv")
