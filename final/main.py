from weather import WeatherAPI
from cat import CatFact_API

def main():
    """
    Initializes WeatherAPI and CatFact_API calls both to get weather and fact then prints out weather along with a random cat fact
    """
    weather = WeatherAPI()
    cat = CatFact_API()
    cat.get_fact()
    city , state = input("Which city and state do you want the weather for (enter separated by comma)?").split(",")
    city_key = weather.getCity(city, state)
    weather.getWeather(city_key)
    print(weather)
    print("Here is a random cat fact: " + str(cat))
    
    
if __name__ == "__main__":
    main()