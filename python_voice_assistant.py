import datetime
import os
import sys
import webbrowser
from time import sleep
import pyautogui
import pyttsx3
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()


def speak(text):
	engine.say(text)
	engine.runAndWait()


def greetings():
	hour = datetime.datetime.now().hour
	if 0 <= hour < 12:
		return 'Good Morning sir, have a great day'
	elif 12 <= hour < 18:
		return 'Good Afternoon sir'
	else:
		return 'Good Evening sir'


dictapp= {
	"command prompt": "cmd",
	"paint": "mspaint",
	"word": "winword",
	"excel": "excel",
	"chrome": "chrome",
	"vs code": "code",
	"powerpoint": "powerpnt",
	"notepad": "notepad",
	"calculator": "calc",
	"spotify": "spotify",
	"skype": "skype",
	"telegram": "Telegram.exe",
	"firefox": "firefox",
	"adobe reader": "acrord32",
	"sublime text": "sublime_text",
	"photoshop": "photoshop",
	"discord": "discord",
	"teams": "teams",
	"zoom": "zoom",
	"vlc": "vlc",
	"outlook": "outlook",
	"onenote": "onenote",
	"pycharm": "pycharm"
	# Continue adding applications as needed
}


def openappweb(text):
	speak("Launching, sir")
	if any(ext in text for ext in ['.com', '.co.in', '.org', 'search']):
		text = text.replace("open", "").replace("jarvis", "").replace("launch", "").replace(" ", "")
		webbrowser.open(f"https://www.{text}")
	else:
		for app in dictapp:
			if app in text:
				os.system(f"start {dictapp[app]}")


def closeappweb(text):
	speak("Closing, sir")
	if "tab" in text:
		num_tabs = int(text.split()[0])
		for _ in range(num_tabs):
			pyautogui.hotkey("ctrl", "w")
			sleep(0.5)
		speak("All specified tabs closed")
	else:
		for app in dictapp:
			if app in text:
				os.system(f"taskkill /f /im {dictapp[app]}.exe")


def listen_for_wake_word():
	with sr.Microphone() as source:
		print('Listening for wake word...')
		while True:
			recognizer.adjust_for_ambient_noise(source, duration=0.5)
			recorded_audio = recognizer.listen(source)
			try:
				text = recognizer.recognize_google(recorded_audio, language='en_US')
				text = text.lower()
				if 'guru' in text:
					print('Wake word detected!')
					speak('Hi Sir, How can I help you?')
					return True
			except Exception as ex:
				print("Could not understand audio, please try again.")


def cmd():
	with sr.Microphone() as source:
		print('Clearing background noise... please wait!')
		recognizer.adjust_for_ambient_noise(source, duration=0.5)
		print('Ask me anything...')
		recorded_audio = recognizer.listen(source)
	try:
		text = recognizer.recognize_google(recorded_audio, language='en_US')
		text = text.lower()
		print('Your message:', text)
	except Exception as ex:
		print(ex)
		return
	
	if 'stop' in text:
		speak('Stopping the program. Goodbye!')
		sys.exit()
	elif 'hello' in text:
		greet = greetings()
		speak(greet)
	elif 'open' in text or 'search' in text:
		openappweb(text)
	elif 'close' in text:
		closeappweb(text)
	elif 'time' in text:
		current_time = datetime.datetime.now().strftime('%I:%M %p')
		print(current_time)
		speak(current_time)
	elif 'who is god' in text:
		speak('Ajitheyyy Kadavuleyy')
	elif 'who is cm' in text:
		speak('vijayey Mudhalamaicharey')
	elif 'what is your name' in text:
		speak('My name is Jarvis, Your Artificial Intelligence')


while True:
	if listen_for_wake_word():
		while True:
			if cmd():
				break
