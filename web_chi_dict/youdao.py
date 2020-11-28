from typing import Any

from .glb import *


class WordYouDao(Word):
    json: Any
    pronunciation_types = {
        Pronunciations: {
            US: 'us-phonetic',
            UK: 'uk-phonetic',
            TTS: 'phonetic',
        },
        Pronunciation_URLs: {
            US: 'us-speech',
            UK: 'uk-speech',
            TTS: 'speech',
        },
        Pronunciation_bytes: {},
    }

    def __init__(self, word: str, timeout=10):
        r"""Get the translation and pronunciation and so on of the word by accessing the API"""
        super(WordYouDao, self).__init__(word, timeout)
        self.json = session.get('http://fanyi.youdao.com/openapi.do', params={
            'keyfrom': 'wangtuizhijia',  # 在网上找的 key
            'key': '1048394636',
            'type': 'data',
            'doctype': 'json',
            'version': '1.2',
            'q': word,
        }, timeout=self.timeout).json()
        if self['errorCode'] != 0:
            return
        self.has_word = True
        if 'basic' in self.json and 'speech' in self['basic']:
            self._set_attrs(self['basic'])

    def __getitem__(self, item):
        return self.json[item]
