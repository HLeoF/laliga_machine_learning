import pandas as pd
import numpy as np
import statistics as stat
import seaborn as sns
import matplotlib.pyplot as plt

filename1 ="raw_laliga_teamDF.csv"
filename2 ="raw_laliga_playerDF.csv"
player = pd.read_csv(filename2)
club = pd.read_csv(filename1)

print(player)
print(club)