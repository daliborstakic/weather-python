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

    def get_weather(self):
        """ Returns weather type, e.g. Clouds, Clear """
        return self.data['weather'][0]['main']

    def temperature(self):
        """ Returns a list containing different temperatures and humidity """
        return self.data['main']

if __name__ == '__main__':
    url = "http://api.openweathermap.org/data/2.5/weather?id=792078&units=metric&appid=07b8e95750270c86b32d751ea6719ca6"
    wapp = Weather(url)

    print(wapp.temperature())
