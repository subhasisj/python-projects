import pandas as pd
import time
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

CITIES = ['chicago', 'new york', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ["monday", "tuesday", "wednesday",
        "thursday", "friday", "saturday", "sunday"]


def user_input(message, work_list):

    while True:
        input_selection = input(message).lower()

        if input_selection in work_list:
            break

        if input_selection == 'all':
            break

    return input_selection


def filter_data():

    print('Let\'s explore some US bikeshare data')

    while True:
        city = input('\nWhich city\'s data do you want to explore( chicago, new york city, washington  ): \n').lower()

        if city in CITY_DATA:
            break
        # else: print('please choose a city from the options provided')

    month = user_input('\nAll right! now it\'s time to provide us a month name or just say \'all\' to apply no month filter.'
                       '\n (e.g. all, january, february, march, april, may, june) \n', MONTHS)

    day = user_input('\nOne last thing. Could you type one of the week day you want to analyze?'
                     ' You can type \'all\' again to apply no day filter.'
                     '(e.g. all, monday, sunday)\n', DAYS)
    

    print('=' * 150)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    print('Loading data for the city {}...........'.format( city ) )
    print( '\n' + '-'*100)
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    # extract the day of the week
    df['day_of_the_week'] = df['Start Time'].dt.weekday_name

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month
    if month != 'all':
        month_index = MONTHS.index(month) + 1
        df = df[ df['month'] == month_index ]
    
    # filter by day
    if day != 'all':
        df = df[ df['day_of_the_week'] == day.title() ]

    print(df.head())

    return df

def calculate_time_statistics( df ):
    """returns statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...')

    start_time = time.time()
    common_month       = df[ 'month' ].mode()[0]
    common_day_of_week = df[ 'day_of_the_week' ].value_counts().idxmax()
    common_start_hour  = df['hour'].mode()[0]
    end_time = time.time() - start_time 

    print( 'The most common month is : {}'.format(common_month) )
    print( 'The most common day of week is :{}'.format(common_day_of_week) )
    print( 'The most common start hour is : {}'.format(common_start_hour) )
    print('\n\nCalculated in {} seconds'.format(end_time))
    print( '\n' + '-'*100)



def station_stats( df ):
    print( '\nCalculating The Most Popular Stations and Trip...' )
    start_time = time.time()
    print('\nThe most commonly used start station :{}'.format(df[ 'Start Station' ].value_counts().idxmax() ) )
    print('The most commonly used end station :{}'.format( df[ 'End Station' ].mode()[0] ) )
    start_and_end_station = df[ [ 'Start Station' , 'End Station' ] ].mode().loc[0]
    print('The most commonly start and end station combination is {} and {} '.format(start_and_end_station[0] , start_and_end_station[1]  ) )
    end_time = time.time() - start_time 
    print('\nCalculated in {} seconds'.format(end_time))
    print( '\n' + '-'*100)

def travel_time_stats( df ):
    print( '\nCalculating The Most Popular Stations and Trip...' )
    start_time = time.time()
    print('Total travel time: {}'.format( sum(df['Trip Duration']) ) )
    print('Mean travel time: {}'.format( df['Trip Duration'].mean() ) )
    print('Max travel time: {}'.format( df['Trip Duration'].max() ) )

    # Display the trip duration grouped by user type
    group_by_user_type = df.groupby(['User Type']).sum()['Trip Duration']
    print('\nTrip Duration per User Type : ')
    for index, trip_info in enumerate( group_by_user_type ):
        print('   {} : {}'.format( group_by_user_type.index[index] , trip_info  ))
    end_time = time.time() - start_time 
    print('\nCalculated in {} seconds'.format(end_time))
    print( '\n' + '-'*100)
