import yaml
import pandas as pd
from datetime import datetime
import csv

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)
    locs = config['locations']

    metrics = pd.DataFrame({0: ['Temperature', 'Relative Humidity', 'Dew Point Temperature', 'Wet Bulb',
                'Atmospheric Pressure', 'Wind Speed', 'Heat Index', 'WBGT Index',
                '2 Inch Soil', '4 Inch Soil', '8 Inch Soil', 'Soil Moisture',
                'Solar Radiation', 'Cumulative Rain Since 12:00 AM']})

    out = config['out']

    for query in locs:
        dt = datetime.now() # get date and time
        date = dt.strftime('%Y-%m-%d') # extract date
        time = dt.strftime('%H:%M') # extract time

        url = f'http://weather.uga.edu/?content=calculator&variable=CC&site={query}' # URL for each location

        dfs = pd.read_html(url) # extract dataframes within webpage

        df = dfs[3] # The third indexed data frame typically contains the weather data

        # clean up data frame of formatting and units
        df = df.replace({'&nbsp': '', '&degF': ''}, regex=True)
        df[1] = df[1].replace({'%': '', 'in.': '', 'W/m2': '', 'mph': ''}, regex=True)

        df = pd.merge(metrics, df, how='left', on=0)

        # Add time stamp and location info
        add_df = pd.DataFrame({0: ['Date', 'Time', 'Location'], 1: [date, time, query]})

        # concatenate dataframes, convert metrics to rownames, and transpose
        df = pd.concat([add_df, df]).set_index(0).transpose()

        # Check if output file exists or is empty
        try:
            pd.read_csv(out)
        # If output file doesn't exist or is empty, write file including headers
        except:
            with open(out, 'w', newline='') as f:
                df.to_csv(out, header=True, index = False, na_rep='nan')
        # if output file exists and is not empty, append file
        else:
            with open(out, 'a', newline='') as f:
                obj = csv.writer(f)
                obj.writerow(df.iloc[0])