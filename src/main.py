import sounddevice

from pyttsx3 import init
from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError
from os import path
from threading import Thread
from libs.utils import Utils
from subprocess import Popen
from libs.const import KEYS, CMDS

recognizer = Recognizer()
speaker = init()
utils = Utils()


class Main(Thread):
    def __init__(self, utils, images_folder, KEYS, CMDS):
        Thread.__init__(self)

        self.text = ""
        self.images_folder = images_folder
        self.KEYS = KEYS
        self.CMDS = CMDS
        self.utils = utils
        self.imageProgram = None

        self.listenSpeak()

    def open_image(self):
        image_name = self.text.replace("open ", ".*").replace(" ", ".*")
        finded_image = self.utils.find_file(
            image_name, path.expanduser(self.images_folder)
        )

        if finded_image:
            msg = f"Opening {image_name.replace(".*", "")}..."
            print(finded_image)
            self.utils.messageHandler(speaker, msg)

            self.imageProgram = Popen(["feh", "-F", finded_image[0]])

    def press_command_key(self):
        for key in self.KEYS:
            if key in self.text:
                utils.keepHotKey(self.KEYS[key])
                return

    def run_cmd(self):
        for cmd in self.CMDS:
            if cmd in self.text:
                exec(self.CMDS[cmd])
                return

    def match_cmd(self):
        self.run_cmd()
        self.press_command_key()

    def recognize_cmd(self, audio_data):
        try:
            self.text = recognizer.recognize_google(audio_data)
            print("You said:", self.text)

            self.text = self.text.lower()

            self.match_cmd()

            if "quit" in self.text:
                exit(0)

        except UnknownValueError:
            msg = "Sorry, could not understand your command."
            print(msg)
        except RequestError as e:
            msg = f"Error: Could not request results on speech Recognition service; {e}"
            self.utils.messageHandler(speaker, msg)

    def listenSpeak(self):
        with Microphone() as source:
            msg = "Speak something..."
            self.utils.messageHandler(speaker, msg)

            recognizer.adjust_for_ambient_noise(source)
            audio_data = recognizer.listen(source)

            self.recognize_cmd(audio_data)

            self.listenSpeak()


DIM = Main(utils=utils, images_folder="~/Imagens/", KEYS=KEYS, CMDS=CMDS)
DIM.start()
