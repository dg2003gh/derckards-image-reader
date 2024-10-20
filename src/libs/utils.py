import os, re, psutil
from time import sleep
from pyautogui import hotkey


class Utils:
    def __init__(self):
        self.keepPressing = False

    def find_file(self, pattern, path):
        result = []
        for root, dirs, files in os.walk(path):
            for name in files:
                regex = re.compile(pattern)

                if regex.match(name.lower()):
                    result.append(os.path.join(root, name))
        return result

    def keepHotKey(self, keys):
        self.keepPressing = True

        while self.keepPressing:
            sleep(1)
            hotkey(keys)

    def setKeepPressing(self, state):
        self.keepPressing = state

    def messageHandler(self, speaker, msg):
        print(msg)
        speaker.say(msg)
        speaker.runAndWait()

    def kill(self, proc_pid):
        process = psutil.Process(proc_pid)
        for proc in process.children(recursive=True):
            proc.kill()
        process.kill()
