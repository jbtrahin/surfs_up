# Surfs-Up
Module 9 on using Python, SQLAlchemy, and Flask, analyze and visualize climate data as you prepare to open a surf shop.

## Module Overview
In this module, you’ll spend time with new tools such as SQLite, SQLAlchemy, and Flask to build on your knowledge of SQL database structures and querying methods. You’ll also write and execute Python code in a Jupyter notebook and create graphs using Python.

## Project Overview
In this challenge, we will be finding a few key aspects of Oahu’s seasonal weather data. The investors want to ensure we’ve hit all of the key points before opening a surf shop.

The goals for this challenge are to:
1. Determine key statistical data about the month of July.
2. Determine key statistical data about the month of December.
3. Compare your findings between the month of July and December.
4. Make 2 or 3 recommendations for further analysis.
5. Share your findings in the Jupyter Notebook.

## Resources

- Database: hawaii.sqlite
- Software: Pandas, Jupyter Notebook, Anaconda 4.7.12, Flask 1.1.1, SQLAlchemy 1.3.9, SQLite

## Our Analysis

### 1 - Key differences in weather between June and December.

|Stats All Dates | Stats June | Stats December |
|:-------------: | :--------: | :------------: |
|![alt text](https://github.com/jbtrahin/surfs_up/blob/master/snapshots/all_dates.png) | ![alt text](https://github.com/jbtrahin/surfs_up/blob/master/snapshots/all_dates_june.png) | ![alt text](https://github.com/jbtrahin/surfs_up/blob/master/snapshots/all_dates_september.png)|

#### Observations on how we pulled the data:
- The raw dataset we explored spanned from 01/01/2010 to 08/23/2017.
- Using a filter in the query, we excluded all rows that contained a NaN value as we made the assumption that the station was not able to retrieve a data read on that day.
- We converted the date column to datetime type to be able to manipulate and access a specific month range.

#### Here is what we observe when comparing the three tables:
- There are more data points available for June (1574) than for December (1405) across the dataset. This might suggest a data retrieval issue for one or several of the stations.
- The average daily precipitation is about 0.14 inches in June and about 0.22 inches in December. If we compare to the average of the entire data set (0.16 inches), we notice that June gets 12.5% less rain than overall and December gets 37.5% more rain than overall.
- The standard deviation is about 0.34 inches in June and about 0.54 inches in December. We notice that June's standard deviation is closer the mean than for December. If we compare to the standard deviation of the entire data set (0.47 inches), we notice that December has a higher standard deviation which suggests that they have some heavier days of rain in December compared to June.
- To corroborate this last point, we notice that 75% of the data points are below 0.12 inches in June and below 0.15  inches in December, which is lower than the mean in both cases. When looking at the max for both June and December, we notice that it is 13 standard deviation higher than the mean for June and 29 standard deviation higher than the mean for December. This tells us that there is some outliers in the data set that skewing the right for both months.

### 2 - Recommendations for further analysis.

#### Here is a few recommendations to dive a little deeper in the dataset:
- We could break down the analysis by stations and identify the most reliable station for the date range we're analyzing for. This would help make our analysis more accurate.
- The analysis compares only two months of the year. While we can use these as a reference for the season, it would be interesting to get the statistics for every month to be able to identify the ideal period to start/keep open the business.
- The analysis is done at the month level. Once we've narrowed down the best month to open the business, it would be interesting to look at weekly/daily trends of precipitations for that specific month to identify if there is a pattern over the past 7 years. For example, this could help us predict days of rain in advance and set up discounts on ice cream for those days to keep the business going.
- We noticed that the data set is skewed to the right. It would be worth removing the outliers from the data set to have a more precise mean calculation for both months.
