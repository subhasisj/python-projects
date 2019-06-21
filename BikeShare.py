import numpy as np
import pandas as pd
import bikeshare_utility_functions as utility
import time

city , month , day  = utility.filter_data()

df = utility.load_data( city , month , day  )
print( '\n' + '-'*100)

utility.calculate_time_statistics(df)
utility.station_stats(df)
utility.travel_time_stats(df)
