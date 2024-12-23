import requests

class WeatherAPI:
    """
    Weather API 
    """
    def __init__(self) -> None:
        """
        Initializes the api key and the base url for the api
        """
        self.api_key = "qBcMGjAg1xPDaEYI2E0AsCj6J16jA5tN" #"5LfalVFvy0OXIYBvwSiY5XDPx6b8mO1R" 
        self.base_url = "http://dataservice.accuweather.com"
        
    def getCity(self, city, state):
        """
        Takes in user input of a city and state and returns the city key used for getting the weather

        Args:
            city (str): city that the user wants the weather for
            state (str): state in which the city that the user wants the weather for is located

        Returns:
            str: the string representation of the city key used to find the weather
        """
        url = f"{self.base_url}/locations/v1/search?apikey={self.api_key}&q={city}%20{state}"
        response = requests.get(url).json()
        self.city_key = response[0]["Key"]
        return self.city_key
        
    def getWeather(self, city_key):
        """
        Gets the forecast for the specific city that the user wants // headline, high and low temps and weather for the night and day

        Args:
            city_key (str): The city key used to find the weather for specific city
        """
        url = f"{self.base_url}/forecasts/v1/daily/1day/{city_key}?apikey={self.api_key}"
        response = requests.get(url).json()
        self.headline = response["Headline"]["Text"]
        self.lowest_temp, self.highest_temp = response["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"], response["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]
        self.day_weather, self.night_weather = response["DailyForecasts"][0]["Day"]["IconPhrase"], response["DailyForecasts"][0]["Night"]["IconPhrase"]
        
    def __str__(self):
        """
        str method that returns the forcast

        Returns:
            str: whole forecast formatted in a readable and easy to interpret way
        """
        return f"DAILY FORECAST: \n{self.headline} \nLow of {self.lowest_temp} \nHigh of {self.highest_temp} \nWeather for the day: {self.day_weather} \nWeather for the night: {self.night_weather}"

        
    
