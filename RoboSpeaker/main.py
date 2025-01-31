from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice").Speak

if __name__ == '__main__':
    print("Welcome to RoboSpeaker! I am here to help you speak.")
    while True:
        x = input('Enter what you want me to speak: ')
        if x == 'q':
            print(speak('Thanks for using me!'))  
            break
        speak(x)