install.packages("arulesViz")
install.packages("arules")
library(arulesViz)
library(tidyverse)
library(dplyr)
library(arules)

setwd("D:/PycharmProjects/pythonProject/laliga_machine_learning/laligaProject/ARM")

player <- read.csv("clean_laliga_playerDF.csv")
club <- read.csv("clean_laliga_teamDF.csv")

### Processing Data Paparation for club dataset
club$goal_against <- club$goal_against_away+club$goal_against_home
club$wins <- club$win_home+club$win_away
club$draws <- club$draw_away+club$draw_home
club$PTS <- club$wins*3 + club$draws
club <- club[c("season", "teamName","PTS")]

#### Processing Data Paparation for player dataset
player$rate_saved <- player$goal_saved / (player$goal_saved + player$goal_conceded + player$penalty_saved)
player <- player[c("season","teamName","position","game_minutes","rate_saved","rating")]
player <- subset(player, position == "Goalkeeper")
player <- subset(player, game_minutes > 95)

#Combine Two Dataset
df <- merge(club, player, by = c("season", "teamName"))
head(df,10)

#Processing Dataset transform to Transacation Data
df <- df[c("game_minutes","rating","rate_saved","PTS")]
df1 <- df %>%
  mutate(game_minutes= case_when(
    game_minutes < 1140 ~ "LessTime_Games",
    game_minutes >= 1140 & game_minutes < 2280 ~ "NormalTime_Games",
    game_minutes >= 2280 ~ "LargeTime_Games"
  ))%>%
  mutate(rating= case_when(
    rating < 6.5 ~ "Bad_Preformance",
    rating >= 6.0 & rating < 6.9 ~ "Normal_Preformance",
    rating >= 6.9 ~ "Good_Preformance"
  ))%>%
  mutate(rate_saved	= case_when(
    rate_saved < 0.45 ~ "Bad_Saved_Skill",
    rate_saved >= 0.45 & rate_saved < 0.69 ~ "Normal_Saved_Skill",
    rate_saved >= 0.69 ~ "Good_Saved_Skill"
  ))%>%
  mutate(PTS	= case_when(
    PTS < 37 ~ "Low_Ranking",
    PTS >= 37 & PTS < 56 ~ "Mid_Ranking",
    PTS >= 56 ~ "High_Ranking"
  ))
head(df1,10)

## Write Transcation Data into a CSV file, and ready to ARM 
write.table(df1, file = "arm.csv", sep = ",", row.names = FALSE, col.names = FALSE, quote = FALSE)

# Read CSV file data as Transaction Data
arm <- read.transactions("arm.csv", 
                         rm.duplicates = FALSE, 
                         format="basket",
                         sep = ",",
                         cols=NULL,
                         header = FALSE)

### Apply ARM rules
rules <- arules::apriori(arm, parameter = list(supp=0.01, conf=0.5, minlen=2))


# 15 Support
support <- sort(rules, by = "support", decreasing = TRUE)
inspect(support[1:15])

subrules <- head(sort(support,by="support"),15)
plot(subrules,method="graph",engine ="interactive")

# 15 Support
confidence <- sort(rules, by = "confidence", decreasing = TRUE)
inspect(confidence[1:15])

