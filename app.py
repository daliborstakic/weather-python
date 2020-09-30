from weather.wgui import AppGUI
from weather.weather import Weather
from tkinter import Tk
import json

if __name__ == '__main__':
    # Loading API url
    with open('api_key.json') as json_file:
        key_dict = json.load(json_file)

    wapp = Weather(key_dict['url'])

    # GUI
    root = Tk()
    gui = AppGUI(root, wapp)
