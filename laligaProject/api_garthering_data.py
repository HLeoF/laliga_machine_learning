import requests
import json as json
import pandas as pd

url = "https://api-football-v1.p.rapidapi.com/v3/teams"

UR_KEY = "41cd2e76d5msh33f2a9a0026698bp1d5129jsnc602132a1e0b"

headers = {
	"X-RapidAPI-Key": UR_KEY ,
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

LALIGA = "140"
TEAMS = 20

team_2020 = []
team_2021 = []
team_2022 = []
team_2023 = []

print("Getting Data From API, Please Wait..........")

def get_teamid(url, headers, query):
  response = requests.get(url, headers=headers, params=query)
  return response

def teamsID_array(parsed,idList):
  for n in range(0,20):
    idList.append(parsed['response'][n]['team']['id'])
  return idList

for y in range(2020,2024):
  querystring = {"league":LALIGA,"season":str(y)}
  response = get_teamid(url, headers, querystring)
  parsed = json.loads(response.text)
  if(y == 2020):
    teamsID_array(parsed,team_2020)
  elif(y == 2021):
    teamsID_array(parsed,team_2021)
  elif(y == 2022):
    teamsID_array(parsed,team_2022)
  else:
    teamsID_array(parsed,team_2023)

# player basic information
teamID = []
team = []
name = []
age = []
birth = []
nationality = []
height = []
weight = []
injured = []
year = []

# player in game
game_appearences = []
game_linups = []
game_minutes = []
game_number = []
game_position = []
game_rating = []
captain = []

# player substiutes
substitu_in = []
substitu_out = []
substitu_bench = []

# player shots
shots_total = []
shots_on = []

# player goals
goal_total = []
goal_conceded = []
goal_assists = []
goal_saves = []

# player passes
pass_tatol = []
key_pass = []
pass_accuracy = []

# player tackles ball
tackle_total = []
blocks = []
interceptions = []

# Duels
duels_total = []
duels_won = []

# player dribbles
dribble_attempts = []
dribble_success = []
dribbles_past = []

# player fouls
fouls_drawn = []
fouls_committed =[]

# Cards
yellow = []
yellowered = []
red = []

# player penalty
penalty_won = []
penalty_commited = []
penalty_scored = []
penalty_missed = []
penalty_saved = []

# team information
team_ID = []
team_Name = []
team_year = []

win_home = []
win_away = []
draw_home = []
draw_away = []
lose_home = []
lose_away = []

goal_for_home = []
goal_for_away = []

goal_against_home = []
goal_against_away = []

url2 = "https://api-football-v1.p.rapidapi.com/v3/players"
url3 = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"


def get_request(url, headers, query):
  response = requests.get(url, headers=headers, params=query)
  return response


def get_player_data(team_id, year):
  for id in team_id:
    qs = {"league":"140","team":str(id),"season":str(year)}
    response = get_request(url2, headers, qs)
    parsed = json.loads(response.text)
    parsed_player_information(parsed)

def get_teams_data(team_id,year):
  for id in team_id:
    qs = {"league":"140","team":str(id),"season":str(year)}
    response = get_request(url3, headers, qs)
    parsed = json.loads(response.text)
    parsed_teams_data(parsed)

def parsed_teams_data(parsed):
  data = parsed['response']
  team_ID.append(data['team']['id'])
  team_Name.append(data['team']['name'])
  team_year.append(data['league']['season'])

  win_home.append(data['fixtures']['wins']['home'])
  win_away.append(data['fixtures']['wins']['away'])
  draw_home.append(data['fixtures']['draws']['home'])
  draw_away.append(data['fixtures']['draws']['away'])
  lose_home.append(data['fixtures']['loses']['home'])
  lose_away.append(data['fixtures']['loses']['away'])

  goal_for_home.append(data['goals']['for']['total']['home'])
  goal_for_away.append(data['goals']['for']['total']['away'])

  goal_against_home.append(data['goals']['against']['total']['home'])
  goal_against_away.append(data['goals']['against']['total']['away'])

def parsed_player_information(parsed):
  data = parsed['response']
  for i in range(0,20):
    info = data[i]['player']
    sta = data[i]['statistics'][0]

    #add player basic information
    teamID.append(sta['team']['id'])
    team.append(sta['team']['name'])
    name.append(info['name'])
    age.append(info['age'])
    birth.append(info['birth']['date'])
    nationality.append(info['nationality'])
    height.append(info["height"])
    weight.append(info['weight'])
    injured.append(info['injured'])
    year.append(sta['league']['season'])

    #add player in game stat information
    game_appearences.append(sta['games']['appearences'])
    game_linups.append(sta['games']['lineups'])
    game_minutes.append(sta['games']['minutes'])
    game_number.append(sta['games']['number'])
    game_position.append(sta['games']['position'])
    game_rating.append(sta['games']['rating'])
    captain.append(sta['games']['captain'])

    # add player substiutes information
    substitu_in.append(sta['substitutes']['in'])
    substitu_out.append(sta['substitutes']['out'])
    substitu_bench.append(sta['substitutes']['bench'])

    # add player shots information
    shots_total.append(sta['shots']['total'])
    shots_on.append(sta['shots']['on'])

    # add player goals information
    goal_total.append(sta['goals']['total'])
    goal_conceded.append(sta['goals']['conceded'])
    goal_assists.append(sta['goals']['assists'])
    goal_saves.append(sta['goals']['saves'])

    # add player passes information
    pass_tatol.append(sta['passes']['total'])
    key_pass.append(sta['passes']['key'])
    pass_accuracy.append(sta['passes']['accuracy'])

    # add player tackles ball information
    tackle_total.append(sta['tackles']['total'])
    blocks.append(sta['tackles']['blocks'])
    interceptions.append(sta['tackles']['interceptions'])

    # add Duels information
    duels_total.append(sta['duels']['total'])
    duels_won.append(sta['duels']['won'])

    # add player dribbles information
    dribble_attempts.append(sta['dribbles']['attempts'])
    dribble_success.append(sta['dribbles']['success'])
    dribbles_past.append(sta['dribbles']['past'])

    # add player fouls information
    fouls_drawn.append(sta['fouls']['drawn'])
    fouls_committed.append(sta['fouls']['committed'])

    # Cards
    yellow.append(sta['cards']['yellow'])
    yellowered.append(sta['cards']['yellowred'])
    red.append(sta['cards']['red'])

    # player penalty
    penalty_won.append(sta['penalty']['won'])
    penalty_commited.append(sta['penalty']['commited'])
    penalty_scored.append(sta['penalty']['scored'])
    penalty_missed.append(sta['penalty']['missed'])
    penalty_saved.append(sta['penalty']['saved'])

print("Gathering Players's Data for each Club.........")
get_player_data(team_2020,2020)
get_player_data(team_2021,2021)
get_player_data(team_2022,2022)
get_player_data(team_2023,2023)
print("Done..........")

print("Gathering Clubs Data.........")
get_teams_data(team_2020,2020)
get_teams_data(team_2021,2021)
get_teams_data(team_2022,2022)
get_teams_data(team_2023,2023)
print("Done........")


print("Creating DataFrames..........")
laliga_df = pd.DataFrame({
    "season":year, "teamId":teamID, "teamName":team, "playerName":name,
    "birthDate":birth, "playerAge":age, "nationality":nationality,
    "height(cm)":height, "weight(kg)":weight, "injured":injured,
    "game_appear":game_appearences, "game_lineups":game_linups, "game_minutes":game_number,
    "number":game_number, "position":game_position, "rating":game_rating,
    "captain":captain,"sub_in":substitu_in, "sub_out":substitu_out,"sub_bench":substitu_bench,
    "shots_total":shots_total, "shots_on":shots_on,"goals_total":goal_total,
    "goal_conceded":goal_conceded, "goal_assists":goal_assists, "goal_saved": goal_saves,
    "pass_total":pass_tatol,"key_pass":key_pass, "pass_accura":pass_accuracy,
    "tackle_total":tackle_total,"tackle_blocks":blocks, "tackle_intercep":interceptions,
    "duel_total":duels_total,"duel_won":duels_won,"dribble_attemp":dribble_attempts,
    "dribble_success":dribble_success, "dribble_past":dribbles_past,
    "fouls_drawn":fouls_drawn, "fouls_committed":fouls_committed,
    "yellow_card":yellow, "yollowed_card":yellowered,"red_card":red,
    "penalty_won":penalty_won,"penalty_scored":penalty_scored,"penalty_missed":penalty_missed,
    "penalty_saved":penalty_saved

})



laliga_team_df = pd.DataFrame({
    "season": team_year, "teamID":team_ID, "teamName":team_Name,
    "win_home":win_home, "win_away":win_away,
    "draw_home":draw_home, "draw_away":draw_away,
    "lose_home":lose_home, "lose_away":lose_away,
    "goal_for_home":goal_for_home, "goal_for_home":goal_for_home,
    "goal_for_away":goal_for_home, "goal_for_away":goal_for_away,
    "goal_against_home":goal_against_home, "goal_for_away":goal_against_away,
    "goal_against_away":goal_against_home, "goal_for_away":goal_against_away
})
print("Done........")

print("Saving DataFrames As CSV files......")
laliga_team_df.to_csv("raw_laliga_teamDF.csv", index=False)
laliga_df.to_csv("raw_laliga_playerDF.csv", index=False)
print("Successfully Saved, Enjoy :)")


