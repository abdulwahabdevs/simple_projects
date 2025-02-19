from weather_api import get_weather, get_weather_details, Weather

def main():
    while True:
        user_city: str = input('Enter a city name for weather forecast: ')
        # get live data for the inputted city
        try:
            current_weather: dict = get_weather(city_name=user_city, mock=False)
            weather_details: list[Weather] = get_weather_details(current_weather)
            break # exit if exception is not raised

        except Exception as error:
            print(f'ERROR: {error}. Please try again!')



    # Get the current days
    dfmt: str = '%Y/%m/%d'
    days: list[str] = sorted({f'{date.date:{dfmt}}' for date in weather_details})

    for day in days:
        print(day)
        print('--------') # divider

        grouped: list[Weather] = [current for current in weather_details if f'{current.date:{dfmt}}' == day]
        for element in grouped:
            print(element)

        print('') # empty line

if __name__ == '__main__':
    main()