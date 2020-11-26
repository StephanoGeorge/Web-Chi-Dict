from typing import Any

from .glb import session, Word


class WordYouDao(Word):
    json: Any
    pronunciation_type = {
        'us': 'us-',
        'uk': 'uk-',
        'tts': '',
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
        self.has_word = 'web' in self.json

    def __getitem__(self, item):
        return self.json[item]

    def pronounce(self, type_='us', speak=False, threaded=True) -> (str, bytes):
        """
        :param type_: 'us' for USA, 'uk' for UK, 'tts' for Text-to-Speak
        :param speak: Whether to speak
        :param threaded: Whether speak through background thread
        :returns String of the phonetic, Bytes of the pronunciation
        """
        if not self.has_word:
            return '', bytes()
        if 'basic' not in self.json or 'speech' not in self['basic']:
            return '', bytes()
        type_ = self.pronunciation_type[type_]
        pronunciation_name = f'pronunciation_{type_}'
        if not hasattr(self, pronunciation_name):
            pronunciation_url = self['basic'][f'{type_}speech']
            if not pronunciation_url:
                pronunciation_url = self['basic']['speech']
            pronunciation = session.get(pronunciation_url, timeout=self.timeout).content
            setattr(self, pronunciation_name, (self['basic'][f'{type_}phonetic'], pronunciation))
        if speak:
            self.speak(getattr(self, pronunciation_name)[1], threaded=threaded)
        return getattr(self, pronunciation_name)
