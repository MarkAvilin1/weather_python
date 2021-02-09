from tkinter import *
from weather_data import WeatherData

"""Graphical interface to show the weather details"""

img = ""

# Function to get the city name and then show the weather details
def show_info():
    global img
    city = city_text.get()
    if city != "":
        data = WeatherData(city)
        city_name = data.city

        if city_name:

            img = PhotoImage(file=f"icons/{data.icon}.png")
            status["image"] = img

            output["text"] = f"Country: {data.country}\n" \
                             f"City: {city_name}\n" \
                             f"Temperature: {data.temp}"
        else:
            output["text"] = "Please check the city name!"
    else:
        output["text"] = "Please enter a city name!"


window = Tk()

city_text = StringVar()

window.geometry("600x530")
window.title("Weather App")
window.config(padx=100, pady=100, bg="#97E8E8")

city_entry = Entry(textvariable=city_text, font=("Ariel", 24, "bold"))
city_entry.pack()

btn = Button(text="Find", command=show_info, font=("Ariel", 24, "bold"))
btn.pack()

status = Label(image="", bg="#97E8E8")
status.pack()

output = Label(text="", bg="#97E8E8", fg="#F29A0C", font=("Ariel", 24, "bold"))
output.pack()

window.mainloop()