from weather.wgui import AppGUI
from weather.weather import Weather
from tkinter import Tk

if __name__ == '__main__':
    url = "http://api.openweathermap.org/data/2.5/weather?id=792078&units=metric&appid=07b8e95750270c86b32d751ea6719ca6"
    wapp = Weather(url)

    # GUI
    root = Tk()
    gui = AppGUI(root, wapp)
