import pandas as pd

################ Data Transforming ###########################
player = pd.read_csv("clean_laliga_playerDF.csv")
club = pd.read_csv("clean_laliga_teamDF.csv")

df = player[['season','teamName','playerName','position','shots_total','shots_on','goals_total']]
df = df[~df['position'].str.contains("Goalkeeper")] #门将不在考虑范围内，需要去掉
df = df[['season','teamName','playerName','shots_total','shots_on','goals_total']]
print(df.head(5))

club = club[["season","teamName","win_home","win_away","draw_home","draw_away","lose_home","lose_away"]]
club.loc[:, 'total_win'] = club['win_home'] + club['win_away']
club.loc[:, 'total_draw'] = club['draw_home'] + club['draw_away']
club.loc[:, "PTS"] = (club["total_win"]*3) + club["total_draw"]
club = club[["season","teamName","PTS"]]
print(club.head(5))

clustering_df = pd.merge(df, club, on=['season', 'teamName'])

print(clustering_df.dtypes)

clustering_df.to_csv("clustering_analysis_df.csv")
