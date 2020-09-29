import requests

class Weather():
    def __init__(self, url):
        """ Init method """
        self.url = url
        self.data = requests.get(self.url).json()

if __name__ == '__main__':
    url = "http://api.openweathermap.org/data/2.5/forecast?q=792078?id=524901&APPID=07b8e95750270c86b32d751ea6719ca6"
    wapp = Weather(url)

    # Checking response
    print(wapp.data)