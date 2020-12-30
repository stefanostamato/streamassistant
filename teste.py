# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3
import webbrowser
from pynput import keyboard

# Initialize the recognizer
r = sr.Recognizer()

#hotkey pra ativar o loop de listen do bot
hotkey = keyboard.Key.alt_gr

# The currently active modifiers
current = set()

def on_press(key):
    print("pressed " + str(key))
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    print("released " + str(key))
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

# The key combination to check
COMBINATIONS = [
    {hotkey}
]

# Function to convert text to
# speech
def SpeakText(command):

    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# Loop infinitely for user to
# speak

def execute():
    print ("Do Something")

    while(hotkey in current):

        # Exception handling to handle
        # exceptions at the runtime
        try:

            # use the microphone as source for input.
            with sr.Microphone() as source2:

                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)


                #listens for the user's input
                audio2 = r.listen(source2)

                # Using ggogle to recognize audio
                MyText = r.recognize_google(audio2, language='pt-BR')
                MyText = MyText.lower()

                print("Did you say "+MyText)
                SpeakText(MyText)

                url = "https://www.google.com.tr/search?q={}".format(MyText)
                webbrowser.open_new_tab(url)

                break


        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occured")

#inicializacao da checagem de hotkey
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
