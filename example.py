from web_chi_dict import WordICiBa, WordYouDao

word = WordICiBa('hot')
print(word.word)  # hot
# print(word.json)  # Full json response
print(word['exchange']['word_third'][0])  # Gets from json
phonetic, pronunciation = word.pronounce()
word.pronounce(speak=True)  # Speak, 'us' for USA, 'uk' for UK, 'tts' for Text-to-Speak

word = WordYouDao('hot')
print(word['basic']['explains'])  # Gets from json
word.pronounce(type_='uk', speak=True)  # Speak, 'us' for USA, 'uk' for UK, 'tts' for Text-to-Speak
