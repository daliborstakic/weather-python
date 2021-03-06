import requests

class Weather():
    def __init__(self, url):
        """ Init method """
        self.url = url
        self.data = requests.get(self.url).json()

    @property
    def city_name(self):
        """ Returns city name """
        return self.data['name']

    @property
    def weather(self):
        """ Returns weather type, e.g. Clouds, Clear """
        return self.data['weather'][0]['main']

    def temperature(self):
        """ Returns a dict containing different temperatures and humidity """
        return self.data['main']
    
    def wind(self):
        """ Returns dict containing wind parameters """
        return self.data['wind']
