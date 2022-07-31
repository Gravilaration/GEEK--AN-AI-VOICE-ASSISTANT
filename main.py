import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyaudio
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import requests
import randfacts
import time
from plyer import notification
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from playsound import playsound

engine=pyttsx3.init() #initialises the pyttsx3 module

voices=engine.getProperty('voices')
for voice in voices: #for changing voice to female
    engine.setProperty('voice', voice.id)

rate = engine.getProperty('rate') #for changing speed to speak
engine.setProperty('rate', rate-30)

def speak(audio):
    engine.say(audio) # convert the written text into speech
    engine.runAndWait() #Pauses the program till the say function is working

def timenow():
    Time=datetime.datetime.now().strftime("%I:%M")
    speak("The current time is")
    speak(Time)#Will speak the current time from your device

def date():
    year=int(datetime.datetime.now().year)#.year will store the year in the year variable
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def welcome():
    hour=datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good Morning!!. I am Geek. How can I help You Today?")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!!. I am Geek. How can I help You Today?")
    elif hour>=18 and hour<=24:
        speak("Good Evening!!. I am Geek. How can I help You Today?")
    else:
        speak("Good Night!!. I am Geek. How can I help You Today?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognising...")
            query=r.recognize_google(audio,language = 'en-in')
        except Exception as e:
            print("Error :  " + str(e))
            speak("Repeat the speech again")
            return "None"
        return query

def email(to,message):
    server=smtplib.SMTP("smtp.gmail.com", 587) #587 is port number for SMTP for secure mail delivery
    server.ehlo()
    server.starttls() #for checking the connection
    server.login("xyz@gmail.com", "xyz@1@2")
    server.sendmail("xyz@gmail.com",to,message)
    server.close()

def screenshot():
    img=pyautogui.screenshot()
    img.save(r"C:\Users\abhin\Downloads\Documents\image.png")

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at" + usage)
    battery=psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

def weatherreport():
    speak("Welcome to the Weather Forecaster!")
    speak("Name the City you want the weather report for!!")

    city_name = takeCommand()

    # Function to Generate Report
    def Gen_report(C):
        url = 'https://wttr.in/{}'.format(C)
        try:
            data = requests.get(url)
            T = data.text
        except:
            T = "Error Occurred"
        print(T)

    Gen_report(city_name)

def facts():
    for i in range(3):
        x = randfacts.get_fact(True)
        speak(x)

def wateralarm():
    notification.notify(
        title="**Please Drink Water Now!!",
        message="Drinking Water Helps to Maintain the Balance of Body Fluids.",
        timeout=10
    )
    time.sleep(60)

if __name__=="__main__":
    welcome()
    while True:
        query=takeCommand().lower()
        print(query)

        if "time" in query:
            timenow()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            try:
                speak("Please wait!. I am getting the information.")
                query=query.replace("wikipedia","") #replaces the word wikipedia from what user what to search
                result=wikipedia.summary(query,sentences=2) #return summary to the searched text's whole content
                speak(result)
            except Exception as e:
                speak("Sorry!!. No pages found!!")
        elif "send email" in query:
            try:
                speak("Speak the message. Please!!")
                content=takeCommand()
                to="abc@gmail.com"
                email(to,content)
                speak("Email sent successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message!!")
        elif "search in browser" in query:
            speak("what you want me to search for you?")
            search=takeCommand().lower()
            wb.open(search)
        elif "logout" in query:
            os.system("shutdown-l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown-/r /t 1")
        elif "play songs" in query:
            songspath= "C:\\Users\\abhin\\Downloads\\Music"
            songs=os.listdir(songspath)
            os.startfile(os.path.join(songspath, songs[0]))
        elif "remember that" in query:
            speak("What you want me to remember?")
            data=takeCommand()
            speak("you said to remember me" + data)
            remember=open("data.txt","w")
            remember.write(data)
            remember.close()
        elif "am i forgetting anything" in query:
            remember=open("data.txt","r")
            speak("you said me to remember that" + remember.read())
        elif "take a screenshot" in query:
            screenshot()
            speak("Screenshot Taken Successfully")
        elif "cpu" in query:
            cpu()
        elif "joke" in query:
            jokes()
        elif "weather" in query:
            weatherreport()
        elif "facts" in query:
            facts()
        elif "water alarm" in query:
            wateralarm()
            speak("It's time to drink water!!")
        elif "pomodoro" in query:
            speak("Starting Pomodoro Timer. Enjoy Your Productive Time")


            class Pomodoro:
                def __init__(self, root):
                    self.root = root

                def work_break(self, timer):

                    # common block to display minutes
                    # and seconds on GUI
                    minutes, seconds = divmod(timer, 60)
                    self.min.set(f"{minutes:02d}")
                    self.sec.set(f"{seconds:02d}")
                    self.root.update()
                    time.sleep(1)

                def work(self):
                    timer = 25 * 60
                    while timer >= 0:
                        pomo.work_break(timer)
                        if timer == 0:
                            # once work is done play
                            # a sound and switch for break
                            playsound("sound.ogg")
                            messagebox.showinfo(
                                "Good Job", "Take A Break, \
            					nClick Break Button")
                        timer -= 1

                def break_(self):
                    timer = 5 * 60
                    while timer >= 0:
                        pomo.work_break(timer)
                        if timer == 0:
                            # once break is done,
                            # switch back to work
                            playsound("sound.ogg")
                            messagebox.showinfo(
                                "Times Up", "Get Back To Work, \
            					nClick Work Button")
                        timer -= 1

                def main(self):

                    # GUI window configuration
                    self.root.geometry("450x455")
                    self.root.resizable(False, False)
                    self.root.title("Pomodoro Timer")

                    # label
                    self.min = tk.StringVar(self.root)
                    self.min.set("25")
                    self.sec = tk.StringVar(self.root)
                    self.sec.set("00")

                    self.min_label = tk.Label(self.root,
                                              textvariable=self.min, font=(
                            "arial", 22, "bold"), bg="red", fg='black')
                    self.min_label.pack()

                    self.sec_label = tk.Label(self.root,
                                              textvariable=self.sec, font=(
                            "arial", 22, "bold"), bg="black", fg='white')
                    self.sec_label.pack()

                    # add background image for GUI using Canvas widget
                    canvas = tk.Canvas(self.root)
                    canvas.pack(expand=True, fill="both")
                    img = Image.open('pomodoro.jpg')
                    bg = ImageTk.PhotoImage(img)
                    canvas.create_image(90, 10, image=bg, anchor="nw")

                    # create three buttons with countdown function command
                    btn_work = tk.Button(self.root, text="Start",
                                         bd=5, command=self.work,
                                         bg="red", font=(
                            "arial", 15, "bold")).place(x=140, y=380)
                    btn_break = tk.Button(self.root, text="Break",
                                          bd=5, command=self.break_,
                                          bg="red", font=(
                            "arial", 15, "bold")).place(x=240, y=380)

                    self.root.mainloop()


            if __name__ == '__main__':
                pomo = Pomodoro(tk.Tk())
                pomo.main()
        elif "play games" in query:
            wb.open("https://www.247games.com/")
        else:
            wb.open(query)

