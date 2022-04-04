import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please choose a city: chicago, new york city or washington\n').lower()
    while city not in CITY_DATA:
        print('invalid city name\n')
        city = input('Please choose a city: chicago, new york city or washington\n').lower()

    # get user input for month (all, january, february, ... , june)
    Monthstest = ["january", "february", "march", "april", "may", "june", "all"]
    month = input('Please choose a month from january to june: to display all months just type all\n').lower()
    while month not in Monthstest:
        print('invalid month name\n')
        month = input('Please choose a month from january to june: to display all months just type all\n').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    daytest = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"]
    day = input('Please choose a day: to display all days just type all\n').lower()
    while day not in daytest:
        print('invalid day name\n')
        day = input('Please choose a day: to display all days just type all\n').lower()

    print('-' * 40)
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
    df['day_of_week'] = df['Start Time'].dt.day_name

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
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # display the most common month
    # extract month from the Start Time column to create a month column
    df['Pmonth'] = df['Start Time'].dt.month_name

    # find the most popular month
    popular_month = df['Pmonth'].mode()

    print('Most Popular Start Month:', popular_month)

    # display the most common day of week
    # extract hour from the Start Time column to create an hour column
    df['Pday'] = df['Start Time'].dt.day_name

    # find the most popular hour
    popular_day = df['Pday'].mode()

    print('Most Popular Start day of the week:', popular_day)

    # display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['Phour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['Phour'].mode()

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    mostcommonstart = df['Start Station'].mode()
    mostcommonend = df['End Station'].mode()
    df["newroute"] = df["Start Station"] + ">" + df["End Station"]
    endandstart = df["newroute"].mode()
    print(
        f"Most commonly used start station: {mostcommonstart} \nMost commonly used end station: {mostcommonend} \nMost frequent combination of start station and end station trip: {endandstart}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_trip = df["Trip Duration"].sum()

    # display mean travel time
    mean_trip = df["Trip Duration"].mean()
    print(f"total trip duration {total_trip} , mean trip duration {mean_trip}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()

    print("user types ",user_types)

    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()

        print("gender ",gender)

        # Display earliest, most recent, and most common year of birth
        earliestYear = df['Birth Year'].min()
        recentYear = df['Birth Year'].max()
        commonYear = df['Birth Year'].mode()[0]
        print(f"earliest year: {earliestYear} ,most racent year: {recentYear} ,common year: {commonYear}")
    except KeyError:
        print("This data is not available")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def raw_data(df):
    dataresponse = input("would you like to see raw data? enter yes  or no")
    while dataresponse == "yes":
        print(df.sample(5))
        dataresponse = input("would you like to see more raw data? enter yes  or no")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
