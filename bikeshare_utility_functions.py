CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = [ 'chicago' , 'new york' , 'washington' ]

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]              

def user_input( message , work_list ):
    
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
        city = input( 'Which city\'s data do you want to explore : \n'
                        'chicago \n'
                        'new york city \n'
                        'washington \n').lower()

        if city in CITY_DATA:
            break
        # else: print('please choose a city from the options provided')

    month = user_input('All right! now it\'s time to provide us a month name or just say \'all\' to apply no month filter.'
                            '\n (e.g. all, january, february, march, april, may, june) \n' , MONTHS)

    day = user_input('One last thing. Could you type one of the week day you want to analyze?'
                      ' You can type \'all\' again to apply no day filter.'
                      '(e.g. all, monday, sunday)\n', DAYS)                                


    return city , month , day                               