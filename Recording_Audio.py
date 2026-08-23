# First Import The Required Libraries

import sounddevice as sd
import wavio
import whisper
import time
import webbrowser
import os
import sys

# Important Parameters 

Sample_rate =16000
Duration_sec =2
FileName = "Bassant.wav"

# Importing The Model

print(" Wait until loading the whisper model.....")
model = whisper.load_model("base")
print("Model loaded successfuly")

# Defining important Functions

def record_to_wav():
     print(f"recording {Duration_sec} seconds ......speak now ")
     audio = sd.rec(int(Duration_sec * Sample_rate), samplerate = Sample_rate , channels =1, dtype="int16")
     sd.wait()
     wavio.write(FileName,audio,Sample_rate,sampwidth =2 )
     print(f"Saved Recording to {FileName}")

def transcribe(FileName):
     result = model.transcribe(FileName)
     text = result["text"].strip().lower()
     print(f" You Said :  {text}")
     return text
def excute_command(command):
     if "open google" in command or command =="google":
          webbrowser.open("https://www.google.com")
          print("Opening Google")

     elif "time" in command:
          current_time = time.strftime("%H:%M:%S")
          print(f"The Current Time Is {current_time}")

     elif "open youtube" in command or command =="youtube":
           webbrowser.open("https://www.youtube.com")    
           print("Opening YouTube")

     elif "notepad" in command or "text editor" in command:
           print("Opening Text Editor")
           if sys.platform == "win32":
                os.system("notepad")
           elif sys.platform == "darwin":
                os.system("open -a TextEdit")
           elif sys.platform == "linux":
                os.system("gedit")

     elif "calculator" in command:
           print("Opening Calculator")
           if sys.platform == "win32":
                os.system("calc")
           elif sys.platform == "darwin":
                os.system("open -a Calculator")
           elif sys.platform == "linux":
                os.system("gnome-calculator")

     elif "exit" in command or "quit" in command:
           print("Exiting....." )
           return False
     else:
          print(" Unkown Command ")
     return True

# Main Functionality of The Code

while True:
     record_to_wav()
     text = transcribe(FileName)
     excute_command(text)
     


