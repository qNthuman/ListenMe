AUTHOR = "RMJ" 

# Importing all the required modules
import tkinter as tk # we would use tk for gui
import speech_recognition as sr 
import pyautogui as pyt 
import time
# The Project Starts here


ListenMe = tk.Tk() # Making our root for the application

#--Functions--#

def openSoftware(voice):
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





def listen():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1) # Most of the devices have 1 index , if this doesn't work try other numbers.
    with mic as source: # Taking the mic as source
        print("I am you assitant ... please order the task...") # adding a print statement to Notify the user 
        r.adjust_for_ambient_noise(source) #just to reduce noise
        audio = r.listen(source) #take voice input from the microphone
        
            
    
    print(r.recognize_google(audio)) #to print voice into text
    voice_str = str(r.recognize_google(audio))
    print(type(voice_str))
    if "open" in voice_str:
        return openSoftware(voice_str)




ListenMe.title("ListenMe") # Title of our application
ListenMe.geometry("334x202+32+32")

ListenButton = tk.Button(ListenMe,text="Speak!",command=listen).grid() # Packing the button



ListenMe.mainloop() # Mainloop of our application
