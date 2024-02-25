install.packages("stylo")
install.packages("factoextra")
library(tidyverse)
library(cluster)
library(factoextra)
library(stylo) ## for using dis cosine

# Set the absolute file path
setwd("D:/PycharmProjects/pythonProject/laliga_machine_learning/laligaProject/clustering")

#Read the csv file
hclust_df <- read.csv('clustering_analysis_df.csv')

#Select shots_total, shots_on, and goals_total variables
data <- hclust_df[, 5:7]
data_scl <- scale(data) # scale data
dist_df <- stylo::dist.cosine(data_scl) # compute cosine Cosine Similarity
hc <- hclust(dist_df, method = "complete") # using cop
plot(hc, cex = 0.1, hang = -1, main = "Cosine Similarity",labels = hclust_df$playerName)
rect.hclust(hc, k = 3, border = 2:5)



tree_height <-1.9 # cut tree height from the original hclust
clus <- cutree(hc, h = tree_height)
temp <- data[clus == 1, ]

temp_dist <- stylo::dist.cosine(scale(temp)) 
temp_hc <- hclust(temp_dist, method = "complete")

l <- hclust_df$playerName[clus == 1]

plot(temp_hc, cex = 0.7, hang = -30, main = "Cosine Similarity", labels = l)
rect.hclust(temp_hc, k = 2, border = 2:5)

df <- paste( hclust_df$teamName[clus == 2], hclust_df$playerName[clus == 2], hclust_df$season[clus == 2],sep ='-')
df <- data.frame(df)
colnames(df)[1] <- "info"
df <- df[grepl("2020", df$info) & (grepl("Barcelona|Atletico Madrid|Real Madrid", df$info)), ]
print(df)


df1 <- paste( hclust_df$teamName[clus == 3], hclust_df$playerName[clus == 3], hclust_df$season[clus == 3],sep ='-')
df1 <- data.frame(df1)
colnames(df1)[1] <- "info"
df1 <- df1[grepl("2020", df1$info) & (grepl("Barcelona|Atletico Madrid|Real Madrid", df1$info)), ]
print(df1)


df2 <- paste( hclust_df$teamName[clus == 1], hclust_df$playerName[clus == 1], hclust_df$season[clus == 1],sep ='-')
df2 <- data.frame(df2)
colnames(df2)[1] <- "info"
df2 <- df2[grepl("2020", df2$info) & (grepl("Barcelona|Atletico Madrid|Real Madrid", df2$info)), ]
print(df2)




