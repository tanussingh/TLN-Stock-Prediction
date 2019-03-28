#   By: Tanushri Singh
#   Teammates:- Nickolas, Lawrence
#   CS 6375 - Machine Learning
#   Instructor: Anjum Chida

###################
#WHAT IT SHOULD DO:-
#This python file will be the Graphical User Interface for the project
###################

#Import Libaries
from tkinter import *

class GUI:
    def window():
        rootWindow = Tk()                   #Constructor rootWindow - main window
        rootWindow.geometry("550x750")
        title = Label(rootWindow, text = "Weather Forecast", bg = "cyan", fg = "white")
        title.config(font = ("verdana", 50))
        title.pack(fill=X)
        citiesTitle = Label(rootWindow, text = "Choose from the following cities: ", bg = "cyan", fg = "blue")
        citiesTitle.config(font = ("Arial", 25))
        citiesTitle.pack(fill=X)

        b1 = Button(text = "Portland, OR", fg = "black")
        b2 = Button(text = "San Francisco, CA", fg = "black")
        b3 = Button(text = "Seattle, WA", fg = "black")
        b4 = Button(text = "Los Angeles, CA", fg = "black")
        b5 = Button(text = "San Diego, CA", fg = "black")
        b6 = Button(text = "Las Vegas, NV", fg = "black")
        b7 = Button(text = "Phoenix, AZ", fg = "black")
        b8 = Button(text = "Albuquerque, NM", fg = "black")
        b9 = Button(text = "Denver, CO", fg = "black")
        b10 = Button(text = "San Antonio, TX", fg = "black")
        b11 = Button(text = "Dallas, TX", fg = "black")
        b12 = Button(text = "Houston, TX", fg = "black")
        b13 = Button(text = "Kansas City, MO", fg = "black")
        b14 = Button(text = "Minneapolis, MN", fg = "black")
        b15 = Button(text = "Saint Louis, MO", fg = "black")
        b16 = Button(text = "Chicago, IL", fg = "black")
        b17 = Button(text = "Nashville, TN ", fg = "black")
        b18 = Button(text = "Indianapolis, IN", fg = "black")
        b19 = Button(text = "Atlanta, GA", fg = "black")
        b20 = Button(text = "Detroit, MI", fg = "black")
        b21 = Button(text = "Jacksonville, FL", fg = "black")
        b22 = Button(text = "Charlotte, NC", fg = "black")
        b23 = Button(text = "Miami, FL", fg = "black")
        b24 = Button(text = "Pittsburg, PA", fg = "black")
        b25 = Button(text = "Philadelphia, PA", fg = "black")
        b26 = Button(text = "New York, NY", fg = "black")
        b27 = Button(text = "Boston, MA", fg = "black")

        #Display the buttons:-
        b1.place(height = 40 , width = 150, x = 20, y = 110)
        b2.place(height = 40 , width = 150, x = 20, y = 165)
        b3.place(height = 40 , width = 150, x = 20, y = 220)
        b4.place(height = 40 , width = 150, x = 20, y = 275)
        b5.place(height = 40 , width = 150, x = 20, y = 330)
        b6.place(height = 40 , width = 150, x = 20, y = 385)
        b7.place(height = 40 , width = 150, x = 20, y = 440)
        b8.place(height = 40 , width = 150, x = 20, y = 495)
        b9.place(height = 40 , width = 150, x = 20, y = 550)
        b10.place(height = 40 , width = 150, x = 200, y = 110)
        b11.place(height = 40 , width = 150, x = 200, y = 165)
        b12.place(height = 40 , width = 150, x = 200, y = 220)
        b13.place(height = 40 , width = 150, x = 200, y = 275)
        b14.place(height = 40 , width = 150, x = 200, y = 330)
        b15.place(height = 40 , width = 150, x = 200, y = 385)
        b16.place(height = 40 , width = 150, x = 200, y = 440)
        b17.place(height = 40 , width = 150, x = 200, y = 495)
        b18.place(height = 40 , width = 150, x = 200, y = 550)
        b19.place(height = 40 , width = 150, x = 380, y = 110)
        b20.place(height = 40 , width = 150, x = 380, y = 165)
        b21.place(height = 40 , width = 150, x = 380, y = 220)
        b22.place(height = 40 , width = 150, x = 380, y = 275)
        b23.place(height = 40 , width = 150, x = 380, y = 330)
        b24.place(height = 40 , width = 150, x = 380, y = 385)
        b25.place(height = 40 , width = 150, x = 380, y = 440)
        b26.place(height = 40 , width = 150, x = 380, y = 495)
        b27.place(height = 40 , width = 150, x = 380, y = 550)

        dateLabel = Label(rootWindow, text = "Choose Date: ", fg = "blue")
        dateLabel.config(font = ("Arial", 25))
        dateLabel.place(x = 15, y = 600)
        inputDate = Entry(rootWindow)
        inputDate.place(height = 40, width = 230, x = 200, y = 600)

        outputLabel = Label(rootWindow, text = "Prediction: ", fg = "blue")
        outputLabel.config(font = ("Arial", 25))
        outputLabel.place(x = 15, y = 655)

        accuracyLabel = Label(rootWindow, text = "Accuracy Details: ", fg = "blue")
        accuracyLabel.config(font = ("Arial", 25))
        accuracyLabel.place(x = 15, y = 710)

        rootWindow.mainloop()               #Ensures window constantly displays until closed

    window()
