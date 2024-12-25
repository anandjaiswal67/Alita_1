import tkinter as tk
from tkinter import* 
from tkinter.ttk import Combobox
import tkintermapview
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage

from opencage.geocoder import OpenCageGeocode
from api import apl


root = Tk()
root.geometry("500x500")

Label_1  = Label(text="number tracker")
Label_1.pack()
numder = Text(height= 1 )
numder.pack()

def getResult():
    num = numder.get("1.0",END)
    num1 = phonenumbers.parse(num)
    locations = geocoder.description_for_number(num1,"en")
    service_s = carrier.name_for_number(num1,"en")

    ocg = OpenCageGeocode(apl)
    query = str(locations)
    result = ocg.geocode(query)
    
    # lat = result[0]['geometry']["lat"]
    # lng = result[0]['geometry']["lng"]
    
    # result.insert(END,"The country of this numder is =  " + locations)
    # result.insert(END,"\n The sim card of this numder is = " + service_s)


button = Button(text="Search", takeCommand = getResult)
button.pack(pady= 10, padx= 100)

result = Text(height=7)
result.pack()

root.mainloop()