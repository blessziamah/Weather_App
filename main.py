from tkinter import *
import requests
import json

root = Tk()
root.title = "MyWeather"
root.geometry("550x100")


# global my_label


def search():
	try:
		api_request = requests.get(
			f"http://api.weatherapi.com/v1/current.json?key=1995a835668c481588742524220612&q={location.get()}&aqi=no")

		api = json.loads(api_request.content)
		city = api['location']['name']
		time = api['location']['localtime']
		temp_c = api['current']['temp_c']
		temp_f = api['current']['temp_f']
	except Exception as e:
		api = "Error....."

	my_label = Label(root, text=f"City: {city}, Time: {time}, TC: {temp_c}, TF: {temp_f}", font="Hervertica, 15")
	my_label.grid(row=1, column=0, columnspan=2, pady=10, padx=10)


location = Entry(root, width=60)
location.grid(row=0, column=0, pady=10, padx=10)

search_btn = Button(root, text="Search", command=search, width=15)
search_btn.grid(row=0, column=1, padx=10)

root.mainloop()
