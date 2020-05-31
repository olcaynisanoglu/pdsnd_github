# -*- coding: utf-8 -*-
"""
Created on Sun May 31 18:36:57 2020

@author: TCONISANOGLU
add  comment
"""

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        print_raw_data = input('\nWould you like to see raw data? Enter yes or no.\n')
        if print_raw_data.lower() == 'yes':
           with open("{}.csv".format(city), "r") as f:
                i = 0
                while print_raw_data.lower() != 'no':
                      for i, line in enumerate(f):
                          i += 1
                          print(line)
                          if i % 5 != 0:
                             continue
                          else:
                             break
                      print_raw_data = input('\nWould you like to continue to see raw data? Enter yes or no.\n')
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
