import requests

class Weather():
    def __init__(self, url):
        """ Init method """
        self.url = url
        self.data = requests.get(self.url).json()

    @property
    def city_name(self):
        return self.data['name']

if __name__ == '__main__':
    url = "http://api.openweathermap.org/data/2.5/weather?id=792078&units=metric&appid=07b8e95750270c86b32d751ea6719ca6"
    wapp = Weather(url)
