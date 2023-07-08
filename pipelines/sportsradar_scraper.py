import os
import json
import random
import requests
import datetime as dt
from dotenv import load_dotenv
from pprint import pprint
from typing import Any



for _ in range(2):
    try:
        SportradarAPI = 'http://api.sportradar.us'
        SPORTRADAR_API_BASE_URI = 'http://api.sportradar.us'
        SPORTRADAR_NCAAMB_API_KEY = os.environ['SPORTRADAR_NCAAMB_API_KEY']
        SPORTRADAR_NCAAWB_API_KEY = os.environ['SPORTRADAR_NCAAWB_API_KEY']
    except KeyError:
        load_dotenv()
        continue


def get_season_id(season: str):
    """Get a given season ID"""
    # TODO: Add support for season IDs
    pass

def get_tournament_id(tournament: str):
    """Get a given tournament ID"""
    # TODO: Add support for tournament IDs
    pass


def get_game_id(team_id: str, game_date: dt.date):
    pass

def get_team_id(season_id: str, school_name: str, mascot_name: str):
    pass

def get_player_id(team_id: str, player_name: str):
    pass



# %%
# Construct the URI for the API endpoint
# ======================================

def construct_pbp_uri(game_id: str, file_type: str = 'json'):
    """Construct the URI for the play-by-play data"""
    api_key = os.environ['SPORTSRADAR_NCAAMB_API_KEY']
    return '{base_uri}/ncaamb/trial/v8/en/games/{game_id}/pbp.{file_type}?api_key={api_key}'.format(base_uri=SportradarAPI, game_id=game_id, file_type=file_type, api_key=api_key)

def construct_team_roster_uri(team_id: str, file_type: str = 'json'):
    """Construct the URI for the team profile data"""
    api_key = os.environ['SPORTSRADAR_NCAAMB_API_KEY']
    return '{base_uri}/ncaamb/trial/v8/en/teams/{team_id}/profile.{file_type}?api_key={api_key}'.format(base_uri=SportradarAPI, team_id=team_id, file_type=file_type, api_key=api_key)

def construct_player_profile_uri(player_id: str, file_type: str = 'json'):
    """Construct the URI for the player profile data"""
    api_key = os.environ['SPORTSRADAR_NCAAMB_API_KEY']
    return '{base_uri}/ncaamb/trial/v8/en/players/{player_id}/profile.{file_type}?api_key={api_key}'.format(base_uri=SportradarAPI, player_id=player_id, file_type=file_type, api_key=api_key)

def construct_season_schedule_uri(season_year: int, season_type: str = 'REG', file_type: str = 'json'):
    """Construct the URI for the season schedule data"""
    api_key = os.environ['SPORTSRADAR_NCAAMB_API_KEY']
    return '{base_uri}/ncaamb/trial/v8/en/games/{season_year}/{season_type}/schedule.{file_type}?api_key={api_key}'.format(base_uri=SportradarAPI, season_year=season_year, season_type=season_type, file_type=file_type, api_key=api_key)

def construct_daily_schedule_uri(year: int, month: int, day: int, file_type: str = 'json'):
    """Construct the URI for the daily schedule data"""
    api_key = os.environ['SPORTSRADAR_NCAAMB_API_KEY']
    return '{base_uri}/ncaamb/trial/v8/en/games/{year}/{month}/{day}/schedule.{file_type}?api_key={api_key}'.format(base_uri=SportradarAPI, year=year, month=month, day=day, file_type=file_type, api_key=api_key)

def construct_tournament_schedule_uri(tournament_id: str, file_type: str = 'json'):
    """Construct the URI for the tournament schedule data"""
    api_key = os.environ['SPORTSRADAR_NCAAMB_API_KEY']
    return '{base_uri}/ncaamb/trial/v8/en/tournaments/{tournament_id}/schedule.{file_type}?api_key={api_key}'.format(base_uri=SportradarAPI, tournament_id=tournament_id, file_type=file_type, api_key=api_key)

# %%
# Construct the filepath for the data
# ===================================

def construct_pbp_filepath(game_id: str, file_type: str = 'json'):
    """Construct the filepath for the play-by-play data"""
    return f'./data/pbp_data/game_{game_id}.{file_type}'

def construct_team_roster_filepath(team_id: str, file_type: str = 'json'):
    """Construct the filepath for the team roster data"""
    return f'./data/team_roster/team_{team_id}.{file_type}'

def construct_player_profile_filepath(player_id: str, file_type: str = 'json'):
    """Construct the filepath for the player profile data"""
    return f'./data/player_profile/player_{player_id}.{file_type}'

# %%
# Call the API endpoints
# ======================

def fetch_season_schedule_data(season_year: int, season_type: str = 'REG', file_type: str = 'json'):
    """Get the schedule data for the entire season"""
    request_uri = construct_season_schedule_uri(season_year, season_type, file_type)

    response = requests.get(request_uri, allow_redirects=True)
    if response.status_code != 200:
        raise Exception('Error: {}'.format(response.status_code))
    
    return response.json()

def fetch_daily_schedule_data(year: int, month: int, day: int, file_type: str = 'json'):
    """Fetch the schedule data for a specific day"""
    request_uri = construct_daily_schedule_uri(year, month, day, file_type)

    response = requests.get(request_uri, allow_redirects=True)
    if response.status_code != 200:
        raise Exception('Error: {}'.format(response.status_code))
    
    return response.json()

def fetch_tournament_schedule_data(tournament_id: str, file_type: str = 'json'):
    """Fetch the schedule data for a specific tournament"""
    request_uri = construct_tournament_schedule_uri(tournament_id, file_type)

    response = requests.get(request_uri, allow_redirects=True)
    if response.status_code != 200:
        raise Exception('Error: {}'.format(response.status_code))
    
    return response.json()

def fetch_team_roster_data(team_id: str, file_type: str = 'json'):
    """Fetch the team roster data"""
    request_uri = construct_team_roster_uri(team_id, file_type)

    response = requests.get(request_uri, allow_redirects=True)
    if response.status_code != 200:
        raise Exception('Error: {}'.format(response.status_code))
    
    return response.json()

def fetch_player_profile_data(player_id: str, file_type: str = 'json'):
    """Fetch the player profile data"""
    request_uri = construct_player_profile_uri(player_id, file_type)

    response = requests.get(request_uri, allow_redirects=True)
    if response.status_code != 200:
        raise Exception('Error: {}'.format(response.status_code))
    
    return response.json()

def fetch_pbp_data(game_id: str, file_type: str = 'json'):
    """Fetch the play-by-play data"""
    request_uri = construct_pbp_uri(game_id, file_type)

    response = requests.get(request_uri, allow_redirects=True)
    if response.status_code != 200:
        raise Exception('Error: {}'.format(response.status_code))
    
    return response.json()


# %%
# Write the data to a file
# ========================

def write_team_roster_data(team_id: str, team_roster_data: dict, *, file_type: str = 'json') -> str:
    """Save the team profile data to a specified file type"""
    filepath = construct_team_roster_filepath(team_id, file_type)    
    with open(filepath, 'w') as f:
        json.dump(team_roster_data, f)
    return filepath

def write_player_profile_data(player_id: str, player_profile_data: dict, *, file_type: str = 'json') -> str:
    """Save a players' profile data to a specified file type"""
    filepath = construct_player_profile_filepath(player_id, file_type)
    with open(filepath, 'w') as f:
        json.dump(player_profile_data, f)
    return filepath

def write_pbp_data(game_id: str, pbp_data: dict, *, file_type: str = 'json') -> str:
    """Save a game's play-by-play data to a specified file type."""
    filepath = construct_pbp_filepath(game_id, file_type)
    with open(filepath, 'w') as f:
        json.dump(pbp_data, f)
    return filepath

# %%
# Read the data from a file
# =========================

def read_pbp_data(filepath: str, *, file_type: str = 'json') -> dict:
    """Read a game's play-by-play data from a specified file type."""
    with open(filepath, 'r') as f:
        return json.load(f)
    
def read_team_roster_data(filepath: str, *, file_type: str = 'json') -> dict:
    """Read a team's roster data from a specified file type."""
    with open(filepath, 'r') as f:
        return json.load(f)
    
def read_player_profile_data(filepath: str, *, file_type: str = 'json') -> dict:
    """Read a player's profile data from a specified file type."""
    with open(filepath, 'r') as f:
        return json.load(f)

# %%
# Application Driver
# ==================

def main():
    # Given a season, get all the team ids & game ids. Save them to a file.
    # For each team id, get the team roster data & player ids. Save the roster data to a file.
    # For each player id, get the player profile data. Save the profile data to a file.
    # For each game id, get the play-by-play data & boxscore data. Save the data to a file.

    season = '2022-23'
    
    team_id = 'c10544de-e3bd-4776-ba2e-83df8c017fd1'
    roster_file = construct_team_roster_filepath(team_id)
    if os.path.exists(roster_file):
        print('Team roster file exists, skipping download...')
        roster_data = read_team_roster_data(roster_file)
    else:
        roster_data = fetch_team_roster_data(team_id)
        write_team_roster_data(team_id, roster_data)
    print('Team Profile Data:', type(roster_data))
    pprint(roster_data)
    print()

    team_players = roster_data['players']
    print('Team Players:', type(team_players))
    pprint(team_players)
    print()

    player = random.choice(team_players)
    print('Player:', player)
    print()

    player_id = player['id']
    print('Player ID:', player_id)
    print()

    player_profile_file = construct_player_profile_filepath(player_id)
    if os.path.exists(player_profile_file):
        print('Player profile file exists, skipping download...')
        player_profile_data = read_player_profile_data(player_profile_file)
    else:
        player_profile_data = fetch_player_profile_data(player_id)
        write_player_profile_data(player_id, player_profile_data)
    print('Player Profile Data:', type(player_profile_data))
    pprint(player_profile_data)
    print()

    game_id = 'c3344171-2527-4ad6-b927-6c700d64c71f'
    pbp_file = construct_pbp_filepath(game_id)
    if os.path.exists(pbp_file):
        print('Play-by-Play file exists, skipping download...')
        pbp_data = read_pbp_data(pbp_file)
    else:
        pbp_data = fetch_pbp_data(game_id)
        write_pbp_data(game_id, pbp_data)
    print('Play-by-Play Data:', type(pbp_data))
    print(pbp_data)
    

if __name__ == '__main__':
    print()
    main()
    print()