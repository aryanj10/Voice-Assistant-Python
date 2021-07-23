import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        clock = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + clock)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'search' in command:
        query = command.replace('search', '')
        talk('searching for' + query)
        webbrowser.open('https://www.google.com/search?q=' + query)
    elif 'intern' in command:
        talk('opening attendance portal')
        webbrowser.open('https://ims-frontend-prod.azurewebsites.net/')
    elif 'message' in command:
        talk('whom do you want to message')
        name = take_command()
        # Replace below path with the absolute path
        # to chromedriver in your computer
        driver = webdriver.Chrome('C:\\Users\\aryan\\OneDrive\\Desktop\\chromedriver')

        driver.get("https://web.whatsapp.com/")
        wait = WebDriverWait(driver, 0)

        # Replace 'Friend's Name' with the name of your friend
        # or the name of a group
        target = name
        talk('what do you want to message to' + name)
        string = take_command()
        talk('messaging' + name + string)
        # Replace the below string with your own message
        time.sleep(15)
        x_arg = '//span[contains(@title,' + target + ')]'
        group_title = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        group_title.click()
        inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
        input_box = wait.until(EC.presence_of_element_located((
            By.XPATH, inp_xpath)))
        for i in range(100):
            input_box.send_keys(string + Keys.ENTER)
            time.sleep(1)
    elif 'portal' in command:
        talk('opening portal')
        webbrowser.open('https://portal.svkm.ac.in/usermgmt/login')
    elif 'teams' in command:
        talk('opening teams')
        webbrowser.open('https://teams.microsoft.com/')
    elif 'college mail' in command:
        talk('opening college mail')
        webbrowser.open('https://mail.google.com/mail/u/5/#inbox')
    elif 'my mail' in command:
        talk('opening personal mail')
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
