import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("clean_laliga_playerDF.csv")
df.head(5)

df['shot_success_rate'] = df['goals_total'] / df['shots_total']
df['duel_success_rate'] = df['duel_won'] / df['duel_total']
df['dribble_success_rate'] = df['dribble_success'] / df['dribble_attemp']
player = df[['season', 'teamName', 'playerName', 'position', 'game_appear', 'game_lineups',
             'game_minutes', 'shot_success_rate', 'duel_success_rate', 'dribble_success_rate',
             'key_pass', 'pass_accura', 'fouls_drawn']]
player = player[player['season'].isin([2020, 2021, 2022])]
player = player[player['position'] == "Attacker"]
player = player.dropna()

### Add labels for each catgory
fig, axes = plt.subplots(3, 3, figsize=(15, 15))

sns.boxplot(x="game_appear", data=player, ax=axes[0, 0])
axes[0, 0].set_title('Game Appearances')

sns.boxplot(x="game_lineups", data=player, ax=axes[0, 1])
axes[0, 1].set_title('Game Lineups')

sns.boxplot(x="game_minutes", data=player, ax=axes[0, 2])
axes[0, 2].set_title('Game Minutes')

sns.boxplot(x="shot_success_rate", data=player, ax=axes[1, 0])
axes[1, 0].set_title('Shot Success Rate')

sns.boxplot(x="duel_success_rate", data=player, ax=axes[1, 1])
axes[1, 1].set_title('Duel Success Rate')

sns.boxplot(x="dribble_success_rate", data=player, ax=axes[1, 2])
axes[1, 2].set_title('Dribble Success Rate')

sns.boxplot(x="key_pass", data=player, ax=axes[2, 0])
axes[2, 0].set_title('Key Pass')

sns.boxplot(x="pass_accura", data=player, ax=axes[2, 1])
axes[2, 1].set_title('Pass Accuracy')

sns.boxplot(x="fouls_drawn", data=player, ax=axes[2, 2])
axes[2, 2].set_title('Fouls Drawn')


def game_appear_label(value):
    if value > 34:
        return 'Good'
    elif value >= 16 and value <= 34:
        return "Normal"
    elif value < 16:
        return "Bad"


def game_lineups_label(value):
    if value > 26:
        return 'Good'
    elif value >= 7 and value <= 26:
        return "Normal"
    elif value < 7:
        return "Bad"


def game_minutes_label(value):
    if value > 2400:
        return 'Good'
    elif value >= 600 and value <= 2400:
        return "Normal"
    elif value < 600:
        return "Bad"


def shot_success_rate_label(value):
    if value > 0.3:
        return 'Good'
    elif value >= 0.08 and value <= 0.3:
        return "Normal"
    elif value < 0.08:
        return "Bad"


def duel_success_rate_label(value):
    if value > 0.45:
        return 'Good'
    elif value >= 0.37 and value <= 0.45:
        return "Normal"
    elif value < 0.37:
        return "Bad"


def dribble_success_rate_label(value):
    if value > 0.6:
        return 'Good'
    elif value >= 0.42 and value <= 0.6:
        return "Normal"
    elif value < 0.42:
        return "Bad"


def key_pass_label(value):
    if value > 30:
        return 'Good'
    elif value >= 6 and value <= 30:
        return "Normal"
    elif value < 6:
        return "Bad"


def pass_accura_label(value):
    if value > 15:
        return 'Good'
    elif value >= 8 and value <= 15:
        return "Normal"
    elif value < 8:
        return "Bad"


def fouls_drawn_label(value):
    if value > 39:
        return 'Good'
    elif value >= 16 and value <= 39:
        return "Normal"
    elif value < 16:
        return "Bad"


player['game_appear_labels'] = player['game_appear'].apply(game_appear_label)
player['game_lineups_labels'] = player['game_lineups'].apply(game_lineups_label)
player['game_minutes_labels'] = player['game_minutes'].apply(game_minutes_label)
player['shot_success_rate_labels'] = player['shot_success_rate'].apply(shot_success_rate_label)
player['duel_success_rate_labels'] = player['duel_success_rate'].apply(duel_success_rate_label)
player['dribble_success_rate_labels'] = player['dribble_success_rate'].apply(dribble_success_rate_label)
player['key_pass_labels'] = player['key_pass'].apply(key_pass_label)
player['pass_accura_labels'] = player['pass_accura'].apply(pass_accura_label)
player['fouls_drawn_labels'] = player['fouls_drawn'].apply(fouls_drawn_label)

cols = ['game_appear_labels', 'game_lineups_labels', 'game_minutes_labels',
        'shot_success_rate_labels', 'duel_success_rate_labels', 'dribble_success_rate_labels',
        'key_pass_labels', 'pass_accura_labels', 'fouls_drawn_labels']

player['label'] = player[[col for col in cols]].mode(axis=1)[0]
player = player[['season', 'teamName', 'playerName', 'position', 'game_appear',
                 'game_lineups', 'game_minutes', 'shot_success_rate',
                 'duel_success_rate', 'dribble_success_rate', 'key_pass',
                 'pass_accura', 'fouls_drawn', 'label']]
player.head(5)
player['label'] = player['label'].astype('category')
player.to_csv("label_clean_DF.csv")