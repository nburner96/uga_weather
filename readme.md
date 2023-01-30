# UGA Weather Scraper
This program can be used to scrape weather from the [UGA weather website](http://weather.uga.edu/). This process can be automated scrape at set intervals using the Task Scheduler program if on Windows(or whatever the Mac equivalent is). The past and historical data on the weather website does not contain all of the same weather metrics that are available for each location at a given time. Therefore, this program allows for the collection of high resolution weather data from throughout the great state of Georgia.

## Tutorial
1. Download [Python](https://www.python.org/downloads/) or [Anaconda](https://www.anaconda.com/) if you haven't already
2. Install the packages found in main.py if you don't already have them
3. Edit the config.yaml file with the desired locations to scrape weather data from and the desired file output name
4. In the downloaded folder, create a .bat file containing the line `python [path]\main.py`
5. In the Task Scheduler program (Windows), click `Create Task...`
6. In the `General` tab, select `Run whether user is logged on or not` and `Run with highest privileges`
7. In the `Triggers` tab, create a new trigger and set the desired interval for running the script. *Note: keep in mind that the weather website typically takes about 5 minutes to post updates every quarter hour, and therefore setting a task to run on the hour for example will provide with the XX:45 weather*
8. Under the `Actions` tab, create a new action and select `Start a program` from the dropdown. Under `Program/script`, paste the path to the .bat file
9. Under `Conditions` select only `Wake the computer to run this task` and `Start only if the following network connection is available`, selecting `Any connection`
10. Lastly, under `Settings`, make sure `Run task as soon as possible after a scheduled start is missed` is selected. Change the other settings as you see fit.
11. The script should automatically run. Be sure to periodically check the CSV output file to make sure everything's running properly