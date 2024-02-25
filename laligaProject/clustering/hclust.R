install.packages("stylo")
install.packages("factoextra")
library(tidyverse)
library(cluster)
library(factoextra)


library(stylo)

setwd("D:/PycharmProjects/pythonProject/laliga_machine_learning/laligaProject/clustering")

hclust_df <- read.csv('clustering_analysis_df.csv')

data <- hclust_df[, 5:7]
data_scl <- scale(data)
dist_df <- stylo::dist.cosine(data_scl)
hc <- hclust(dist_df, method = "complete")
plot(hc, cex = 0.1, hang = -1000, main = "Cosine",labels = hclust_df$playerName)

cut_height <- 1.3
cutree_result <- cutree(hc, h = cut_height)
clipped_data <- data[cutree_result == 1, ]

clipped_dist <- stylo::dist.cosine(scale(clipped_data))
clipped_hc <- hclust(clipped_dist, method = "complete")

l <- hclust_df$playerName[cutree_result == 1]

plot(clipped_hc, cex = 0.5, hang = -30, main = "Cosine", labels = l)
