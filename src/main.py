import speech_recognition as sr
import sounddevice
import pyttsx3

from os import path
from threading import Thread
from libs.utils import Utils
from subprocess import Popen
from libs.const import KEYS, CMDS

recognizer = sr.Recognizer()
speaker = pyttsx3.init()
utils = Utils()


def press_command_key(text):
    for key in KEYS:
        if key in text:
            utils.keepHotKey(KEYS[key])


def run_cmd(text):
    for cmd in CMDS:
        if cmd in text:
            exec(CMDS[cmd])


def match_cmd(text):
    run_cmd(text)
    press_command_key(text)


def recognize_cmd(audio_data):
    global imageProgram

    try:
        text = recognizer.recognize_google(audio_data)
        print("You said:", text)

        text = text.lower()

        if "open" in text:
            image_name = text.replace("open ", ".*").replace(" ", ".*")
            finded_image = utils.find_file(image_name, path.expanduser("~/Imagens/"))

            if finded_image:
                msg = f"Opening {image_name.replace(".*", "")}..."
                utils.messageHandler(speaker, msg)

                imageProgram = Popen(["feh", "-F", finded_image[0]])

        if "quit" in text:
            exit(0)

        matches = Thread(target=match_cmd, args=([text.replace(" ", "_")]))
        matches.start()

    except sr.UnknownValueError:
        msg = "Sorry, could not understand your command."
        print(msg)
    except sr.RequestError as e:
        msg = f"Error: Could not request results on speech Recognition service; {e}"
        utils.messageHandler(speaker, msg)

    listenSpeak()


def listenSpeak():
    with sr.Microphone() as source:
        msg = "Speak something..."
        utils.messageHandler(speaker, msg)
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio_data = recognizer.listen(source, timeout=5)

        recognize_cmd(audio_data)


Thread(target=listenSpeak).start()
