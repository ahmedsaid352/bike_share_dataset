import datetime
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
            'new york city': 'new_york_city.csv',
            'washington': 'washington.csv' }

expectedCities =["chicago", "new york city","washington"]
expectedMonths = ['january', 'february', 'march', 'april', 'may', 'june','all']
expectedDays = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']

all_msgs =['yes','ye','y','ok','no','n']
accept_msgs =['yes','ye','y','ok']
refuse_msgs=['no','n']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\n\n which city you want to hear about? chicago, new york city or washington\n").lower().strip()
        if city  in expectedCities:
            break
        else:
            print("\n please enter a valid city\n")
            print('-'*40)
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\n which month you want all, january, february, ... , june\n ").strip().lower()
        if month  in expectedMonths:
            break
        else:
            print("\n please enter a valid month \n")
            print('-'*40)
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\n please enter the day like : all, monday, tuesday, ... sunday\n").strip().lower()
        if day  in expectedDays:
            break
            print('-'*40)
        else:
            print("\n please enter a valid day\n")
            print('-'*40)
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_of_week

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month =df['month'].mode()[0]
    print("\nthe most common month : ", common_month )

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("\nthe most common day: ", common_day )

    # TO DO: display the most common start hour
    df['hour'] =df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\nMost Frequent Start Hour: ', popular_hour)

    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print("\nthe most common start Station: ", common_start )
    # TO DO: display most commonly used end station

    common_end = df['End Station'].mode()[0]
    print("\nthe most common End Station : ", common_end )
    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + " ==> "+ df['End Station']
    common_trip = df['trip'].mode()[0]
    print("\nmost frequent combination of start station and end station trip : ", common_trip  )
    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()

    print('\n total travel time: ',datetime.timedelta(seconds = float(total_time)))

    # TO DO: display mean travel time
    mean_time = round(df['Trip Duration'].mean(),3)
    print('\n mean travel time: ',datetime.timedelta(seconds = float(mean_time)))

    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    try:

        gender = df['Gender'].value_counts()
        print(gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print("\nthe earliest year of birth : ", int(earliest) )
        print("\nthe most recent year of birth : ", int(recent) )
        print("\nthe most common year of birth : ", int(most_common) )
    except:
        print("\n no data about gender or birth date in washington ")
    print("\nThis took %s seconds." % round((time.time() - start_time),3))
    print('-'*40)

def display_raw_data(df):
    """ printing the next 5 rows until the user chooses 'no'. """
    i = 0
    raw = input("\n do you want to see the first 5 raws of data? yes or no \n").strip().lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i:i+5,]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("\n do you want to see the next 5 raws of data? yes or no \n").strip().lower() # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").strip().lower()
# to handle invalid inputs 
def restart():
    restart_input = input('\nWould you like to restart? Enter yes or no.\n')
    if restart_input.lower() not in all_msgs:
        print('\n please enter valid message, yes or no\n')
        restart()
    elif restart_input.lower() in refuse_msgs:
        quit()
    elif restart_input.lower() in accept_msgs:
        main()

def main():
    city, month, day = get_filters()
    df = load_data(city, month, day)

    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)
    display_raw_data(df)
    restart()


if __name__ == "__main__":
	main()
