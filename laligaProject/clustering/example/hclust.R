library(tidyverse)

df <- read.csv("text.csv")
head(df)

data <- df[2:4]
data_scale <- scale(data)
data_dist1 <- dist(data_scale, method = "euclidean")
data_dist2 <- dist(data_scale, method = "manhattan")
data_display1 <- hclust(data_dist1, method = "complete")
data_display2 <- hclust(data_dist2, method = "complete")
data_display3 <- hclust(data_dist1, method = "single")
data_display4 <- hclust(data_dist1, method = "average")

plot(data_display1)
rect.hclust(data_display1, k=3, border = 2:5)
plot(data_display2)
rect.hclust(data_display2, k=3, border = 2:5)
plot(data_display3)
rect.hclust(data_display3, k=3, border = 2:5)
plot(data_display4)
rect.hclust(data_display4, k=3, border = 2:5)