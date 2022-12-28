AUTHOR = "RMJ" 

# Importing all the required modules
import tkinter as tk # we would use tk for gui
import speech_recognition as sr 
import pyautogui as pyt 
import time
import pyttsx3 as p3 # Importing pyttsx3 for language generation 
import random 
# import pyjokes
# The Project Starts here



class Listen_me:
    def __init__(self) -> None:
        self.Author = "RMj"
        self.Version = "0"
        self.under = "Curios AI"
        self.name = "Curi"

    def speak(self,sentence:str):
        """Language generation for the Bot."""
        engine = p3.init()
        engine.say(sentence)
        engine.runAndWait()

#TODO
#openGit : Open gith with default web browser #

    def introduce(self):
        Greeting = ["Hello", "HI","Bonjour!","Salve!"]
        cGreeting = random.choice(Greeting)
        self.speak(f"{cGreeting} , I am {self.name} . I was made by {self.Author} under{self.under} , my version is {self.Version}.I am not an AI but a Bot designed to automate the daily tasks.")
        

    def joke():
        pass

    def checkTime(self):
        t = time.strftime("%H %M")
        self.speak(t)

    def openGit():
        pass



    def openSoftware(self,voice):
        """Open an application/Software on users command..."""
        voice = voice.split(" ")
        print(voice)
        print(voice.index("open"))
        x = voice.index("open")
        x+=1
        print(voice[x])
        appName = voice[x]

        pyt.moveTo(283,1066) # Add your serach bar locations here
        time.sleep(1)
        pyt.click()
        time.sleep(1) # Adding sleep so that the computer clicks aren't too fast 
        pyt.write(appName)
        time.sleep(1)
        pyt.press("Enter")

    def search(self,voice_input:str):
        voice = voice_input.split("search")
        print(voice)
        print(voice.index(""))
        x = voice.index("")
        x+=1
        print(voice[x])
        search_data = voice[1]

        self.openSoftware("open brave")
        time.sleep(10)
        pyt.hotkey("ctrl","k")
        pyt.write(search_data)


    def listen(self):
        """Listen for the command.."""    
        r = sr.Recognizer()
        mic = sr.Microphone(device_index=1) # Most of the devices have 1 index , if this doesn't work try other numbers.
        with mic as source: # Taking the mic as source
            print("I am you assitant ... please order the task...") # adding a print statement to Notify the user 
            r.adjust_for_ambient_noise(source) #just to reduce noise
            audio = r.listen(source) #take voice input from the microphone
            
                
        
        print(r.recognize_google(audio)) #to print voice into text
        voice_str = str(r.recognize_google(audio)).lower()

        if "open" in voice_str:
            return self.openSoftware(voice_str)
        elif "introduce" in voice_str:
            return self.introduce()
        elif "time" in voice_str:
            return self.checkTime()
        elif "search" in voice_str:
            return self.search(voice_str)
        

        


    def main(self):
        """Main function to handle all other functions."""
        self.listen()

        

if __name__ == "__main__":
    ListenMe = tk.Tk() # Making our root for the application

    app = Listen_me()


    ListenMe.title("ListenMe") # Title of our application
    ListenMe.geometry("334x202+32+32")

    ListenButton = tk.Button(ListenMe,text="Speak!",command=app.listen).grid() # Packing the button



    ListenMe.mainloop() # Mainloop of our application
