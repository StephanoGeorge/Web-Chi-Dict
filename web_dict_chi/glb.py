import subprocess as sp
import tempfile
import threading

import requests

session = requests.Session()


class Word:
    word: str
    has_word: bool = False

    def __init__(self, word: str, timeout: int):
        self.word = word
        self.timeout = timeout

    @classmethod
    def speak(cls, pronunciation, suffix='.mp3'):
        def speak_():
            with tempfile.NamedTemporaryFile('wb', suffix=suffix) as f:
                f.write(pronunciation)
                f.flush()
                # Wait for finish, or the file will be deleted. Execute through shell, or can not get the file
                sp.run(['ffplay', '-nodisp', '-autoexit', f'{f.name}'], stdout=sp.DEVNULL, stderr=sp.DEVNULL)

        threading.Thread(target=speak_).start()
