import os
import re
import json
import wget
import requests
import pandas as pd
import datetime as dt
from prefect import task, flow

    

def extract_from_github(game_id: int = 401522200, game_date: str = '2023-04-03', season: str = '2022-23'):
    """Extract data from GitHub Repo `lbenz730/ncaahoopR_data`"""
    pbp_url = 'https://raw.githubusercontent.com/lbenz730/ncaahoopR_data/master/{season}/pbp_logs/{game_date}/{game_id}.csv'.format
    url = pbp_url(season=season, game_date=game_date, game_id=game_id)
    filename = wget.download(url, 'pbp.csv')
    return filename



def transform_to_parquet(filename: str, game_id: int = 401522200):
    """Transform and clean data from CSV to Parquet"""
    df = pd.read_csv(filename)
    headers = [['game_id','play_id','half','date','home_team','away_team','time_remaining_half',
                'secs_remaining','secs_remaining_absolute','description','action_team','home_score','away_score',
                'referees','arena_location','arena','capacity','attendance','home_coach','away_coach',
                'shot_x','shot_y','shot_team','shot_outcome','shooter','assist','three_pt','free_throw',
                'possession_before','possession_after','wrong_time']]
    df.to_csv(f'pbp_{game_id}.parquet', index=False)
    os.remove(filename)

