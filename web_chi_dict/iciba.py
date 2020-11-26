from typing import Any

from .glb import session, Word


class WordICiBa(Word):
    json: Any
    pronunciation_type = {
        'us': 'am',
        'uk': 'en',
        'tts': 'tts',
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

    def __getitem__(self, item):
        return self.json[item]

    def pronounce(self, type_='us', speak=False) -> (str, bytes):
        """
        :param type_: 'us' for USA, 'uk' for UK, 'tts' for Text-to-Speak
        :param speak: Whether to speak
        :returns String of the phonetic, Bytes of the pronunciation
        """
        if not self.has_word:
            return
        type_ = self.pronunciation_type[type_]
        if 'symbol_mp3' in self['symbols'][0]:
            pronunciation_name = 'pronunciation_cn'
            phonetic_key = 'word_symbol'
            url_key = 'symbol_mp3'
        else:
            pronunciation_name = f'pronunciation_{type_}'
            phonetic_key = f'ph_{type_}'
            url_key = f'ph_{type_}_mp3'
        if hasattr(self, pronunciation_name):
            return getattr(self, pronunciation_name)
        pronunciation_url = self['symbols'][0][url_key]
        if not pronunciation_url:
            pronunciation_url = self['symbols'][0]['ph_tts_mp3']
        pronunciation = session.get(pronunciation_url, timeout=self.timeout).content
        phonetic = self['symbols'][0][phonetic_key] if phonetic_key in self['symbols'][0] else ''
        setattr(self, pronunciation_name, (phonetic, pronunciation))
        if speak:
            self.speak(pronunciation)
        return getattr(self, pronunciation_name)
