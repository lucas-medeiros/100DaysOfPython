import pyttsx3
import speech_recognition as sr
import smtplib
import emails
import time
import keyboard
import wikipedia as wk
import pywhatkit as kit
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyjokes as pj


def send_whatsapp_msg(cont, msg):
    df = pd.read_csv("contacts.csv")
    for index, row in df.iterrows():
        if cont in row["name"]:
            kit.sendwhatmsg_instantly(phone_no=row["number"], message=msg)
            keyboard.press_and_release("ctrl+w")
            time.sleep(4)
            keyboard.press_and_release("Enter")
            return True
    speak_function("Number do not exit in our record")
    insert_new_contact = input("Do you want to add the contact in the contacts_file Y/N:").lower()
    if insert_new_contact == "yes" or insert_new_contact == "y":
        name = input("Enter the name of Contact: ").lower().strip()
        number = input("Enter the number: ").strip()
        new_contact = {
            "name": name,
            "number": number,
        }
        data = df._append(new_contact, ignore_index=True)
        data.to_csv("contacts.csv", index=False)
        speak_function("record added successfully")


def extract_whats_numbers():
    contacts = {
        "name": [],
        "number": [],
    }
    path = "F:/chromedriver/chromedriver-win64/chromedriver.exe"
    headings = ["name", "number"]

    data_frame = pd.DataFrame(columns=headings)
    data_frame.to_csv("contacts.csv", index=False)
    service = Service(executable_path=path)  # your chrome driver path
    option = webdriver.ChromeOptions()

    option.add_experimental_option("detach", True)
    wb = webdriver.Chrome(service=service, options=option)
    wb.get(url="https://web.whatsapp.com/")
    time.sleep(60)

    scroll_amount = 1200
    scroll_element = wb.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div[2]")

    for _ in range(9):
        print("Running!")
        time.sleep(2)
        first = "_8nE1Y"
        header = "AmmtE"
        contact1 = wb.find_elements(By.CLASS_NAME, first)

        for con in contact1:
            con.click()
            contact2 = wb.find_element(By.CLASS_NAME, header)
            contact2.click()
            time.sleep(3)

            try:
                name = wb.find_element(By.XPATH,
                                       "/html/body/div[1]/div/div/div[6]/span/div/span/div/"
                                       "div/section/div[1]/div[2]/h2/span")
                number = wb.find_element(By.XPATH, "/html/body/div[1]/div/div/div[6]/"
                                                   "span/div/span/div/div/section/div[1]/div[2]/div/span/span")

                if name.text not in contacts["name"]:
                    contacts["name"].append(name.text.lower())
                    contacts["number"].append(number.text)
                    new_contact = {
                        "name": name.text.lower(),
                        "number": number.text,
                    }
                    data = pd.read_csv("contacts.csv")
                    data = data.append(new_contact, ignore_index=True)
                    data.to_csv("contacts.csv", index=False)
            except Exception as exp:
                pass
        wb.execute_script("arguments[0].scrollBy(0, arguments[1]);", scroll_element, scroll_amount)
    wb.close()


def play_youtube_video(topic):
    kit.playonyt(topic)


def search_on_google(topic):
    kit.search(topic)


def wiki_information(topic, senten=10):
    search_topic = wk.summary(topic, sentences=senten)
    return search_topic


def speak_function(txt):
    engine = pyttsx3.init()
    engine.setProperty("rate", 180)
    engine.say(txt)
    engine.runAndWait()


def speech_recog():
    print("listening....")
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=None)
            txt = (r.recognize_google(audio))
            return txt.lower()
    except sr.UnknownValueError:
        speak_function("cannot recognize Sir.")
        return "None"


def send_email(rec):

    speak_function("What is subject of email?")
    subject = speech_recog()

    speak_function("Tell me message")
    message = speech_recog()

    if message == "None":
        send_email(rec= receiver)
    user_name = "YOUR_EMAIL_HERE"
    password = "YOUR_PASSWORD_HERE"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user_name, password=password)
        connection.sendmail(from_addr=user_name, to_addrs=rec, msg=f"Subject:{subject}\n\n{message}")


while True:
    query = speech_recog()
    print(query)
    if "send email" in query or "send mail" in query:
        receiver = (query.split("to"))[1].strip()
        print(receiver)
        if receiver in emails.email.keys():
            send_email(rec=emails.email.email[receiver])
            speak_function("message send successfully")

        else:
            speak_function("User is not added in our database")

    elif "send whatsapp message" in query or "send a whatsapp message" in query or "send message on whatsapp" in query:
        try:
            contact = (query.split("to"))[1].strip()
            df = pd.read_csv("contacts.csv")
            speak_function("Tell the message Sir.")
            msg = speech_recog()
            send_whatsapp_msg(cont=contact, msg=msg)
            speak_function("whatsapp message send successfully.")
        except FileNotFoundError:
            speak_function("Sir scan QR code and I am going to extract numbers from your whatsapp I will take some time"
                           " and I may miss some contacts.")
            speak_function("Sir you should have to scan the QR code within 50 sec otherwise contacts file will be empty"
                           " and you should have to delete it and run the script again")
            extract_whats_numbers()

    elif "search in google" in query or "search on google" in query or "on google" in query:
        speak_function("what should I search on google Sir.")
        search = speech_recog()
        search_on_google(topic=search)

    elif "search on wikipedia" in query or "search a wikipedia article" in query or\
            "search article on wikipedia" in query:
        speak_function("On which topic should I search about.")
        article = speech_recog()
        speak_function(wiki_information(topic=article))

    elif "search on youtube" in query or "play a video on youtube" in query or "play on youtube" in query or\
            "on youtube" in query:
        speak_function("On which topic you want to see a video.")
        topic = speech_recog()
        play_youtube_video(topic=topic)

    elif "jarvis i love you" in query or "jarvis i love u" in query:
        speak_function("I to love you Sir! ")

    elif "i want to hear some jokes" in query or "crack some jokes" in query or "i want to hear joke" in query or \
            "joke" in query:
        joke = pj.get_joke("en")
        speak_function(joke)

    elif "news headlines" in query or "i want to hear some news" in query or "today news" in query:
        speak_function("On which topic you want to hear the headline.")
        top = speech_recog()

    elif "shutdown" in query or "jarvis shutdown" in query or "close yourself" in query:
        speak_function("Good bye. Have a nice Day Sir take-care of yourself.")
        break
