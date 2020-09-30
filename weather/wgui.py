from tkinter import Label

class AppGUI():
    def __init__(self, master, app):
        """ Init method """
        self.master = master
        self.app = app

        # City name
        self.city = Label(master, text=app.city_name)
        self.city.grid(row=0, column=0, padx=5, pady=5)

        # Weather
        self.weather = Label(master, text=f"Type: {app.weather}")
        self.weather.grid(row=1, column=0, padx=5, pady=5)

        # Temperature
        self.max_t = Label(master, text=f"Max temperature: {app.temperature()['temp_max']}°C")
        self.max_t.grid(row=2, column=0, padx=5, pady=5)

        self.min_t = Label(master, text=f"Min temperature: {app.temperature()['temp_min']}°C")
        self.min_t.grid(row=2, column=1, padx=5, pady=5)

        self.feels = Label(master, text=f"Feels like: {app.temperature()['feels_like']}°C")
        self.feels.grid(row=3, column=0, padx=5, pady=5)

        # Air pressure
        self.pressure = Label(master, text=f"Pressure: {app.temperature()['pressure']}mbar")
        self.pressure.grid(row=4, column=0, padx=5, pady=5)

        # Humidity
        self.humid = Label(master, text=f"Humidity: {app.temperature()['humidity']}%")
        self.humid.grid(row=4, column=1, padx=5, pady=5)

        # Wind
        self.wind_speed = Label(master, text=f"Wind speed: {app.wind()['speed']}m/s")
        self.wind_speed.grid(row=5, column=0, padx=5, pady=5)

        self.wind_deg = Label(master, text=f"Wind angle: {app.wind()['deg']}°")
        self.wind_deg.grid(row=5, column=1, padx=5, pady=5)

        self.master.mainloop()
