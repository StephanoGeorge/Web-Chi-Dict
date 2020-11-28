from typing import Any

from .glb import *


class WordICiBa(Word):
    json: Any
    pronunciations: dict
    pronunciation_URLs: dict
    pronunciation_bytes: dict
    pronunciation_types = {
        Pronunciations: {
            US: 'ph_am',
            UK: 'ph_en',
            TTS: 'ph_other',
        },
        Pronunciation_URLs: {
            US: 'ph_am_mp3',
            UK: 'ph_en_mp3',
            TTS: 'ph_tts_mp3',
        },
        Pronunciation_bytes: {},
    }

    def __init__(self, word: str, timeout=10):
        r"""Get the translation and pronunciation and so on of the word by accessing the API"""
        super(WordICiBa, self).__init__(word, timeout)
        self.json = session.get('http://dict-co.iciba.com/api/dictionary.php', params={
            'key': '54A9DE969E911BC5294B70DA8ED5C9C4',  # 在网上找的 key, 似乎不限制使用频率
            'type': 'json',
            'w': word,
        }, timeout=self.timeout).json()
        self.has_word = 'word_name' in self.json
        if self.has_word and 'symbol_mp3' not in self['symbols'][0]:
            self._set_attrs(self['symbols'][0])

    def __getitem__(self, item):
        return self.json[item]
