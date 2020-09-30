from tkinter import Label

class AppGUI():
    def __init__(self, master, app):
        """ Init method """
        self.master = master
        self.app = app

        self.city = Label(master, text=app.city_name)
        self.city.grid(row=0, column=0, padx=5, pady=5)