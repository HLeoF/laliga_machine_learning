install.packages("arulesViz")
install.packages("arules")
library(arulesViz)
library(tidyverse)
library(dplyr)
library(arules)

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

subrules1 <- head(sort(confidence,by="confidence", decreasing = TRUE),15)
plot(subrules1,method="graph",engine ="interactive")

#15 Lift
lift <- sort(rules, by = "lift", decreasing = TRUE)
inspect(life[1:15])

subrules2 <- head(sort(lift,by="lift"),15)
plot(subrules2,method="graph",engine ="interactive")
