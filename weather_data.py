import requests

"""Get weather information from the API of https://openweathermap.org"""
class WeatherData:
    KEY = "aba9c361e3bf4c76f293a9bfdf535be7"
    API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather?"

    def __init__(self, city_name):
        self.parameters = {
            "q": city_name,
            "appid": self.KEY
        }
        self.response = requests.get(url=self.API_ENDPOINT, params=self.parameters)
        self.response.raise_for_status()
        self.status = self.response.status_code
        self.data = self.response.json()
        self.country = self.data["sys"]["country"]
        self.city = self.data["name"]
        self.temp = int(self.data["main"]["temp"] - 273.15)
        self.weather = self.data["weather"][0]["main"]
        self.icon = self.data["weather"][0]["icon"]
