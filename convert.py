#!/usr/bin/python3
import pandas as pd
from itertools import groupby 
from collections import OrderedDict
import json    
import codecs

df = pd.read_csv('fpl.csv', dtype={
            "team" : str,
            "position" : str,
            "name" : str,
            "cost" : float,
            "status" : str,
            "minutes" : float,
            "total_points" : int,
            "bonus" : int,
            "points_per_game" : float,
            "selected_by_percent" : float
        }, encoding='utf-8')

results = []

for team, players in df.groupby("team"):
    contents_df = players.drop(["team"], axis=1)
    player = [OrderedDict(row) for i, row in contents_df.iterrows()]
    results.append(OrderedDict([("team", team),
                ("player", player)]))

with codecs.open('mongo_insert_file.json', 'w', 'utf-8') as outfile:
    outfile.write(json.dumps(results, indent=4, ensure_ascii=False))
