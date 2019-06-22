# python-projects

Let's explore some US bikeshare data

Which city's data do you want to explore( chicago, new york city, washington  ):
new york city

All right! now it's time to provide us a month name or just say 'all' to apply no month filter.
 (e.g. all, january, february, march, april, may, june)
january

One last thing. Could you type one of the week day you want to analyze? You can type 'all' again to apply no day filter.(e.g. all, monday, sunday)
may

One last thing. Could you type one of the week day you want to analyze? You can type 'all' again to apply no day filter.(e.g. all, monday, sunday)
wednesday
======================================================================================================================================================
Loading data for the city new york city...........

----------------------------------------------------------------------------------------------------
     Unnamed: 0          Start Time             End Time  Trip Duration            Start Station  ...  Gender Birth Year month  day_of_the_week  hour
15       187466 2017-01-11 11:30:30  2017-01-11 11:35:15            285       E 17 St & Broadway  ...    Male     1972.0     1        Wednesday    11
121      378557 2017-01-18 18:24:36  2017-01-18 18:46:42           1325  Rivington St & Ridge St  ...  Female     1986.0     1        Wednesday    18
150       72902 2017-01-04 23:02:57  2017-01-04 23:05:12            135          2 Ave & E 31 St  ...    Male     1991.0     1        Wednesday    23
311       60804 2017-01-04 16:57:14  2017-01-04 17:06:56            582          5 Ave & E 78 St  ...    Male     1987.0     1        Wednesday    16
382      533071 2017-01-25 08:54:16  2017-01-25 09:03:40            563          1 Ave & E 18 St  ...    Male     1988.0     1        Wednesday     8

[5 rows x 12 columns]

----------------------------------------------------------------------------------------------------

Calculating The Most Frequent Times of Travel...
The most common month is : 1
The most common day of week is :Wednesday
The most common start hour is : 8


Calculated in 0.0 seconds

----------------------------------------------------------------------------------------------------

Calculating The Most Popular Stations and Trip...

The most commonly used start station :Pershing Square North
The most commonly used end station :Pershing Square North
The most commonly start and end station combination is Pershing Square North and Pershing Square North

Calculated in 0.01562190055847168 seconds

----------------------------------------------------------------------------------------------------

Calculating The Most Popular Stations and Trip...
Total travel time: 4382522
Mean travel time: 748.7650777379122
Max travel time: 50586

Trip Duration per User Type :
   Customer : 158317
   Subscriber : 4194728

Calculated in 0.0 seconds

----------------------------------------------------------------------------------------------------

Calculating User Stats...

Total users per user type :
    Subscriber : 5723
    Customer : 109

Counts of gender:
    Male : 4433
    Female : 1232
The most common birth year: 1986.0
The most recent birth year: 2000.0
The most earliest birth year: 1934.0

Calculated in 0.009102344512939453 seconds

----------------------------------------------------------------------------------------------------

Calculating Dataset Stats...
The number of missing values in the new york city dataset:376
The columns have 'NaN' values are :['User Type', 'Gender', 'Birth Year']
The number of missing values in the 'Birth Year' column:167

Would like to see trip details ? Type 'yes' or 'no :
yes
{
  "Birth Year": 1972.0,
  "End Station": "W 17 St & 8 Ave",
  "End Time": "2017-01-11 11:35:15",
  "Gender": "Male",
  "Start Station": "E 17 St & Broadway",
  "Start Time": 1484134230000,
  "Trip Duration": 285,
  "Unnamed: 0": 187466,
  "User Type": "Subscriber",
  "day_of_the_week": "Wednesday",
  "hour": 11,
  "month": 1
}
{
  "Birth Year": 1986.0,
  "End Station": "Montrose Ave & Bushwick Ave",
  "End Time": "2017-01-18 18:46:42",
  "Gender": "Female",
  "Start Station": "Rivington St & Ridge St",
  "Start Time": 1484763876000,
  "Trip Duration": 1325,
  "Unnamed: 0": 378557,
  "User Type": "Subscriber",
  "day_of_the_week": "Wednesday",
  "hour": 18,
  "month": 1
}
{
  "Birth Year": 1991.0,
  "End Station": "E 25 St & 2 Ave",
  "End Time": "2017-01-04 23:05:12",
  "Gender": "Male",
  "Start Station": "2 Ave & E 31 St",
  "Start Time": 1483570977000,
  "Trip Duration": 135,
  "Unnamed: 0": 72902,
  "User Type": "Subscriber",
  "day_of_the_week": "Wednesday",
  "hour": 23,
  "month": 1
}
{
  "Birth Year": 1987.0,
  "End Station": "E 65 St & 2 Ave",
  "End Time": "2017-01-04 17:06:56",
  "Gender": "Male",
  "Start Station": "5 Ave & E 78 St",
  "Start Time": 1483549034000,
  "Trip Duration": 582,
  "Unnamed: 0": 60804,
  "User Type": "Subscriber",
  "day_of_the_week": "Wednesday",
  "hour": 16,
  "month": 1
}
{
  "Birth Year": 1988.0,
  "End Station": "8 Ave & W 16 St",
  "End Time": "2017-01-25 09:03:40",
  "Gender": "Male",
  "Start Station": "1 Ave & E 18 St",
  "Start Time": 1485334456000,
  "Trip Duration": 563,
  "Unnamed: 0": 533071,
  "User Type": "Subscriber",
  "day_of_the_week": "Wednesday",
  "hour": 8,
  "month": 1
}

Would like to see trip details ? Type 'yes' or 'no :
no

Would you like to restart ? Type 'yes' or 'no :
yes
Let's explore some US bikeshare data

Which city's data do you want to explore( chicago, new york city, washington  ):
chicago

All right! now it's time to provide us a month name or just say 'all' to apply no month filter.
 (e.g. all, january, february, march, april, may, june)
all

One last thing. Could you type one of the week day you want to analyze? You can type 'all' again to apply no day filter.(e.g. all, monday, sunday)
all
======================================================================================================================================================
Loading data for the city chicago...........

----------------------------------------------------------------------------------------------------
           Start Time             End Time  Trip Duration                 Start Station                          End Station  ...  Gender Birth Year  month  day_of_the_week hour
0 2017-05-29 18:36:27  2017-05-29 18:49:27            780     Columbus Dr & Randolph St                 Federal St & Polk St  ...    Male     1991.0      5           Monday   18
1 2017-06-12 19:00:33  2017-06-12 19:24:22           1429        Kingsbury St & Erie St  Orleans St & Merchandise Mart Plaza  ...     NaN        NaN      6           Monday   19
2 2017-02-13 17:02:02  2017-02-13 17:20:10           1088         Canal St & Madison St              Paulina Ave & North Ave  ...  Female     1982.0      2           Monday   17
3 2017-04-24 18:39:45  2017-04-24 18:54:59            914  Spaulding Ave & Armitage Ave       California Ave & Milwaukee Ave  ...    Male     1966.0      4           Monday   18
4 2017-01-26 15:36:07  2017-01-26 15:43:21            434        Clark St & Randolph St         Financial Pl & Congress Pkwy  ...  Female     1983.0      1         Thursday   15

[5 rows x 11 columns]

----------------------------------------------------------------------------------------------------

Calculating The Most Frequent Times of Travel...
The most common month is : 6
The most common day of week is :Tuesday
The most common start hour is : 17


Calculated in 0.01562047004699707 seconds

----------------------------------------------------------------------------------------------------

Calculating The Most Popular Stations and Trip...

The most commonly used start station :Streeter Dr & Grand Ave
The most commonly used end station :Clinton St & Washington Blvd
The most commonly start and end station combination is Streeter Dr & Grand Ave and Clinton St & Washington Blvd

Calculated in 0.01052403450012207 seconds

----------------------------------------------------------------------------------------------------

Calculating The Most Popular Stations and Trip...
Total travel time: 375286
Mean travel time: 938.215
Max travel time: 47551

Trip Duration per User Type :
   Customer : 109689
   Subscriber : 265597

Calculated in 0.007968425750732422 seconds

----------------------------------------------------------------------------------------------------

Calculating User Stats...

Total users per user type :
    Subscriber : 330
    Customer : 70

Counts of gender:
    Male : 244
    Female : 86
The most common birth year: 1989.0
The most recent birth year: 1999.0
The most earliest birth year: 1949.0

Calculated in 0.01197195053100586 seconds

----------------------------------------------------------------------------------------------------

Calculating Dataset Stats...
The number of missing values in the chicago dataset:140
The columns have 'NaN' values are :['Gender', 'Birth Year']
The number of missing values in the 'Birth Year' column:70

Would like to see trip details ? Type 'yes' or 'no :
no

Would you like to restart ? Type 'yes' or 'no :
no
