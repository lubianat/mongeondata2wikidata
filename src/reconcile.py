import pathlib
import pandas as pd
from pathlib import Path

HERE = Path(__file__).parent.resolve()
DATA = HERE.parent.joinpath("data").resolve()
RESULTS = HERE.parent.joinpath("results").resolve()

import tweepy
from twitter_keys import *
import time

auth = tweepy.OAuth1UserHandler(
    API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)
mongeon_wikidata_df = pd.read_csv(RESULTS.joinpath("mongeon_to_wikidata.csv"))

quickstatements = []
for i, row in mongeon_wikidata_df.iterrows():
    tweeter_id = row.tweeter_id
    r = api.get_user(user_id=str(tweeter_id))
    handle = r.screen_name
    quickstatements.append(f'{row.author}|P2002|"{handle}"' "|S248|Q113610629")
    time.sleep(0.1)

quickstatements = list(set(quickstatements))
RESULTS.joinpath("quickstatements.txt").write_text("\n".join(quickstatements))
