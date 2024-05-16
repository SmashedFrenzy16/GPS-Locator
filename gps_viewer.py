from tkinter import *
import requests as rq
import folium
import datetime
import time
from tkinter import messagebox
import os
import webbrowser
from tkinterweb import *
import webview

root = Tk()

root.title("GPS Locator")

root.geometry("600x400")

Label(root, fg="red", text="Welcome To GPS Locator App!", font=("Arial", 25)).pack()

blank_label = Label(root, text="").pack()

def gps_tracker():

    global map_gen

    def get_coords():

        try:

            data = rq.get("https://ipinfo.io").json()

            coord_pair = data["loc"].split(",")

            latitude, longitude = float(coord_pair[0]), float(coord_pair[1])

            city = data.get("city", "Unknown")

            region = data.get("region", "Unknown")

            return latitude, longitude, city, region

        except:

            messagebox.showerror("Error: Please check your internet connection and try again.")

            return False

    map_gen = folium.Map(location=[0, 0], zoom_start=2)

    try:

        latitude, longitude, city, region = get_coords()

        label_region = Label(root, text=f"Location: {city}, {region}").pack()

        label_coords = Label(root, text=f"Latitude: {latitude} | Longitude: {longitude}").pack()

        folium.Marker([latitude, longitude], popup="Current Coordinates").add_to(map_gen)

        f_name = "C:/Users/USER/Downloads/" + "map.html" # Replace USER with your username, or change the path if you are on Mac/Linux

        map_gen.save(f_name)

        webview.create_window("Location", f_name) 
        webview.start() 

        return f_name

    except:

        messagebox.showerror("Error: Please check your internet connection and try again.")

        return False

show_location = Button(root, text="Show Location", command=gps_tracker).pack()

root.mainloop()