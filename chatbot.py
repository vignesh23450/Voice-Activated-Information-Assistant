import pyttsx3 as p
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time

class Info:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_info(self, query):
        self.query = query
        self.driver.get(url="http://www.wikipedia.org")

        try:
            search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
            search.click()
            search.send_keys(query)
            enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
            enter.click()

            while True:
                try:
                    # This will raise a WebDriverException if the browser is closed
                    self.driver.title
                    time.sleep(1)
                except WebDriverException:
                    print("Browser closed. Terminating the script.")
                    break
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            try:
                self.driver.quit()
            except:
                pass

engine = p.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 125)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

speak("Hello sir, I am your personal assistant chatbot. How are you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        text = ""

if "what" in text and "about" in text and "you" in text:
    speak("I'm good, looking forward to a great day ahead.")
speak("May I know how can I assist you, sir?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    try:
        text2 = r.recognize_google(audio)
        print(text2)
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        text2 = ""

if "information" in text2:
    speak("You need information on what topic?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        try:
            t3 = r.recognize_google(audio)
            print(t3)
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            t3 = ""

    if t3:
        assist = Info()
        assist.get_info(t3)
