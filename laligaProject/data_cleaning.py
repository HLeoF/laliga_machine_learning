import pandas as pd
import numpy as np
import statistics as stat
import seaborn as sns
import matplotlib.pyplot as plt

filename1 ="raw_laliga_teamDF.csv"
filename2 ="raw_laliga_playerDF.csv"
player = pd.read_csv(filename2)
club = pd.read_csv(filename1)

print(player.columns)
print(player.dtypes)

## drop cloumns
fig, axes = plt.subplots(2, 3, figsize=(15, 8))

# sns.countplot(x="injured", data=player, ax=axes[0][0])
# sns.countplot(x='number', data=player, ax=axes[0][1])
# sns.countplot(x='captain', data=player, ax=axes[0][2])
# sns.countplot(x='game_minutes', data=player, ax=axes[1][0])
# sns.countplot(x='penalty_won', data=player, ax=axes[1][1])
# sns.countplot(x='dribble_past', data=player, ax=axes[1][2])
# plt.show()

p_clean = player.drop(['teamId', 'birthDate','injured',
             'game_minutes','number','captain',
             'penalty_won','dribble_past'], axis=1)

## drop some characters
p_clean['height(cm)'] = p_clean['height(cm)'].str.replace('cm', '')
p_clean['weight(kg)'] = p_clean['weight(kg)'].str.replace('kg', '')
p_clean

## Check missing value
ColumnNamesList = p_clean.columns.values
for name in ColumnNamesList:
    print(name, ": ", end="")
    total_nas=p_clean[name].isna().sum()
    print(total_nas)

### Fill NaN
cols = ['rating','game_appear', 'game_lineups', 'sub_in', 'sub_out', 'sub_bench',
        'shots_total', 'shots_on', 'goals_total', 'goal_conceded',
        'goal_assists', 'goal_saved', 'pass_total', 'key_pass', 'pass_accura',
        'tackle_total', 'tackle_blocks', 'tackle_intercep', 'duel_total',
        'duel_won', 'dribble_attemp', 'dribble_success', 'fouls_drawn',
        'fouls_committed', 'yellow_card', 'yollowed_card', 'red_card',
        'penalty_scored', 'penalty_missed', 'penalty_saved']

p_clean[cols] = p_clean[cols].fillna(0)

## chage the data types
p_clean["season"] = p_clean["season"].astype(str)
p_clean["height(cm)"] = pd.to_numeric(p_clean["height(cm)"], errors='coerce')
p_clean["weight(kg)"] = pd.to_numeric(p_clean["weight(kg)"], errors='coerce')
p_clean["position"] = p_clean["position"].astype('category')



height_mean = p_clean['height(cm)'].mean(skipna=True)
weight_mean = p_clean['weight(kg)'].mean(skipna=True)
p_clean['height(cm)'] = p_clean['height(cm)'].fillna(height_mean)
p_clean['weight(kg)'] = p_clean['weight(kg)'].fillna(weight_mean)

## Check missing value
ColumnNamesList = p_clean.columns.values
for name in ColumnNamesList:
    print(name, ": ", end="")
    total_nas=p_clean[name].isna().sum()
    print(total_nas)


#### Check the clubs data
ColumnNamesList = club.columns.values
for name in ColumnNamesList:
    print(name, ": ", end="")
    total_nas=club[name].isna().sum()
    print(total_nas)

print(club.dtypes)

club = club.drop(['teamID'], axis=1)

club['season'] = club['season'].astype(str)

print(club.dtypes)

p_clean.to_csv("clean_laliga_playerDF.csv", index=False)
club.to_csv("clean_laliga_teamDF.csv", index=False)
