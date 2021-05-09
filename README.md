# surfs_up
## Overview of the analysis:
The purpose of this analysis is to help W. Avy who is planning to build a shop at Oahu we need to see the weather patterns of that location Oahu .
### WE can see the following to determine if the location Oahu will be ideal for opening a shop.
#### Precipatation
#### Station
#### Temperature
#### Statistics
One way to provide this insight is with a visualization—we'll plot the results of our precipitation analysis using Matplotlib.
Using statistical analysis—such as the mean, standard deviation, minimum, and maximum will help to determine if investing in the shop at Oahu will be a good idea or not.
It's clear from your analysis that Oahu is a great location for the new surf shop.
There are 9 stations from which precipitation data is being collected,we need to know how active the stations are as well.We need to figure out which stations tend to have the most precipitation recordings,in this case active essentially means the number of recordings for each station.This will help us figure out how reliable our data is, which, in turn, will boost W. Avy's confidence in his investment.Using group by in our query we can determine the station with highest recordings.
The temperature data will determine low,high and average temperature of the location which will help to determine the best weather for surfing and eating ice cream.Using the following functions: func.min, func.max, and func.avg  will help to give the temp recordings
  
SQLite to store the weather data.SQLite provides a quick way to setup a database engine without requiring a server.In order to connect to the SQLite database, we'll use SQLAlchemy.SQLAlchemy will help us easily connect to our database where we'll store the weather data.
W. Avy is concerned about the amount of precipitation on Oahu. There needs to be enough rain to keep everything green, but not so much that you lose out on that ideal surfing and ice cream weather




## Results:
From the query based on the month of June we can see that the temperature is mostly in the 70's 
![](June.png?raw=true)
From the query based on the month of Dec we can see that the temperature is mostly in the 70's 
![](dec.png?raw=true)
From the Stastics for the month of June we can see that the min temp is 64 and the max temp is 85
![](Summary_Stat_June.png?raw=true)
From the Stastics for the month of June we can see that the min temp is 56 and the max temp is 83
![](Summary_Stat_Dec.png?raw=true)


## Summary:


