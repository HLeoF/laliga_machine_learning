import pandas as pd
import numpy as np
import statistics as stat
import seaborn as sns
import matplotlib.pyplot as plt



filename1 ="clean_laliga_teamDF.csv"
filename2 ="clean_laliga_playerDF.csv"
player = pd.read_csv(filename2)
club = pd.read_csv(filename1)

temp = player[['playerName','nationality']]
temp = temp.drop_duplicates(subset=['playerName'])

plt.figure(figsize=(15, 5))
sns.countplot(x="nationality", data=temp, order = temp['nationality'].value_counts().index)
plt.xticks(rotation=90)
plt.title("number of Nationality")
plt.xlabel('Nations')
plt.ylabel('Number')
plt.show()

temp = player
red_df = temp.groupby('teamName')['red_card'].sum().reset_index()
yellow_df = temp.groupby('teamName')['yellow_card'].sum().reset_index()

red_df = red_df.sort_values(by='red_card', ascending=False)
sns.barplot(x="teamName",y='red_card', data=red_df)
plt.xticks(rotation=90)
plt.title("number of Red Card for each club 2020-2023")
plt.xlabel('Clubs')
plt.ylabel('Number')
plt.show()

yellow_df = yellow_df.sort_values(by='yellow_card', ascending=True)
sns.barplot(x="teamName",y='yellow_card', data=yellow_df)
plt.xticks(rotation=90)
plt.title("number of Yellow Card for each club 2020-2023")
plt.xlabel('Clubs')
plt.ylabel('Number')
plt.show()

sns.scatterplot(x = 'playerAge', y = 'goals_total', data = player)
plt.title("Player Age and Total Goal relationship")
plt.xlabel("Player Age")
plt.ylabel("Goal Total")
plt.show()


saved = player.groupby('teamName')['goal_saved'].sum().reset_index()
sns.barplot(x="teamName",y='goal_saved', data=saved)
plt.xticks(rotation=90)
plt.title("number of goal save for each club 2020-2023")
plt.xlabel('Clubs')
plt.ylabel('Number')
plt.show()


cf = club.groupby(['teamName'])[['win_home','win_away','goal_for_home','goal_against_home']].sum().reset_index()
cf['total_win'] = cf['win_home']+cf['win_away']
cf = cf.sort_values(by='total_win', ascending=False)
sns.barplot(x = 'total_win', y = 'teamName', data = cf)
plt.title("Total Wins for Clubs 2020-2023")
plt.xlabel("Number of Total Wins")
plt.ylabel("Clubs")
plt.show()

sns.boxplot(x = 'goal_for_home', data = cf)
plt.xlabel("Goals for Home - Clubs")
plt.show()
sns.boxplot(x = "goal_against_home", data = cf)
plt.xlabel("Goals Against Home - Clubs")
plt.show()

cff = club.groupby(['teamName','season'])[['lose_home','lose_away']].sum().reset_index()
cff['total_lose'] = cff['lose_home']+cff['lose_away']
cff = cff[cff['teamName'].isin(['Atletico Madrid','Barcelona','Sevilla','Athletic Club','Real Madrid'])]
sns.lineplot(x = 'season', y = 'total_lose',hue = 'teamName', data=cff)
plt.title("Total Losses For clubs 2020 TO 2023")
plt.ylabel("Number of Total Loses")
plt.show()