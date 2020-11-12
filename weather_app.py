from tkinter import *
from tkinter import messagebox
import requests
from configparser import ConfigParser
from PIL import ImageTk, Image

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
degree_sign = u"\N{DEGREE SIGN}"

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']


def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city_name = json['name']
        country = json['sys']['country']
        temp_kel = json['main']['temp']
        temp_c = temp_kel - 273.15
        temp_f = (temp_kel - 273.15) * 9 / 5 + 32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city_name, country, int(temp_c), int(temp_f), icon, weather)
        return final
    else:
        return None


def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = f'{weather[0]} {weather[1]}'
        temp_lbl['text'] = f'{weather[2]} {degree_sign}c, {weather[3]} {degree_sign}f'
        weather_lbl['text'] = weather[5]
        my_img = ImageTk.PhotoImage(Image.open(""f'icons/{weather[4]}.png'))
        show_image['image'] = my_img
    else:
        messagebox.showerror('Error', f'Cannot find {city}')


app = Tk()
app.title('Weather App')
app.geometry('400x280')
app.iconbitmap('icons/file.ico')
city_text = StringVar()

label = Label(app, text='Weather Finder')
label.pack()

city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text='Search weather', width=12, command=search)
search_btn.pack()

location_lbl = Label(app, text='', font=('bold', 20))
location_lbl.pack()

show_image = Label(image=None)
show_image.pack()

temp_lbl = Label(app, text='')
temp_lbl.pack()

weather_lbl = Label(app, text='')
weather_lbl.pack()
app.mainloop()
