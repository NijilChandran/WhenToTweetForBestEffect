# WhenToTweetForBestEffect

## 1. Reading the Dataset

Sample File content from tweet_engagements.csv:
```
Date,Impression,Engagement
1.11.2020,506,106
2.11.2020,331,50
3.11.2020,377,86
4.11.2020,333,108
```

## 2. Transforming the Dataset

### Generate a DataFrame that contains week numbers in rows, week day names in columns, and engagement rates as values.
  + Create week of the year column from Date
  + Create day of the week column from Date 
  + Create rate column as Engagement/Impression
  
## 3. Calculating P-Values

### The hypothesis we aim to test is that Friday is the best day to get maximum tweet engagement. 
 + Objective is to calculate the p-values of tweet engagement rates between Friday and other-days 
 + Interpret the significance of the relationship.

## 4. Interpreting the Results

### Make an inference about the hypothesis from previous output
+ Apply Bonferoni correction to the results and interpret them again with adjusted results
