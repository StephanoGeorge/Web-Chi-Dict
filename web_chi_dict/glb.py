import subprocess as sp
import tempfile
import threading

import requests

session = requests.Session()

Pronunciations, Pronunciation_URLs, Pronunciation_bytes = 'pronunciations', 'pronunciation_URLs', 'pronunciation_bytes'
US, UK, TTS = 'us', 'uk', 'tts'


class Word:
    word: str
    has_word: bool = False
    pronunciation_types: dict

    def __init__(self, word: str, timeout: int):
        self.word = word
        self.timeout = timeout

    def _set_attrs(self, container):
        def set_(attr_name, type_):
            key_name = self.pronunciation_types[attr_name][type_]
            if key_name in container and container[key_name]:
                getattr(self, attr_name)[type_] = container[key_name]

        for a, d in self.pronunciation_types.items():
            setattr(self, a, {})
            for t in d.keys():
                set_(a, t)

    def get_pronunciation(self, types=()) -> str:
        pronunciation = self._get_alternative_type(types, Pronunciations)
        if pronunciation:
            return pronunciation[1]
        else:
            return ''

    def speak(self, types=(), threaded=True):
        """
        :param types: See example.py
        :param threaded: Whether speak through background thread
        """
        pronunciation_url = self._get_alternative_type(types, Pronunciation_URLs)
        if not pronunciation_url:
            return
        type_, pronunciation_url = pronunciation_url
        if not pronunciation_url:
            return ''
        pronunciation_byte = getattr(self, Pronunciation_bytes)
        if type_ not in pronunciation_byte:
            pronunciation_byte[type_] = session.get(pronunciation_url, timeout=self.timeout).content

        def play():
            with tempfile.NamedTemporaryFile('wb', suffix='.mp3') as f:
                f.write(pronunciation_byte[type_])
                f.flush()
                # Wait for finish, or the file will be deleted. Execute through shell, or can not get the file
                sp.run(['ffplay', '-nodisp', '-autoexit', f'{f.name}'], stdout=sp.DEVNULL, stderr=sp.DEVNULL)

        if threaded:
            threading.Thread(target=play).start()
        else:
            play()
        return pronunciation_byte[type_]

    def _get_alternative_type(self, types, attr_name):
        if not hasattr(self, attr_name):
            return
        attr = getattr(self, attr_name)
        if not types:
            types = self.pronunciation_types[attr_name].keys()
        for t in types:
            if t in attr and attr[t]:
                return t, attr[t]
