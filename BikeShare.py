import numpy as np
import pandas as pd
import bikeshare_utility_functions as utility
import time


def main():
    while True:
            city , month , day  = utility.filter_data()

            df = utility.load_data( city , month , day  )
            print( '\n' + '-'*100)

            utility.calculate_time_statistics(df)
            utility.station_stats(df)
            utility.travel_time_stats(df)
            utility.calc_user_statistics(df)
            utility.dataset_stats(df, city)
            utility.display_data_in_json_format(df)

            answer = input('\nWould you like to restart ? Type \'yes\' or \'no : \n').lower()        

            if answer != 'yes':
                break

if __name__ == '__main__':
    main()
