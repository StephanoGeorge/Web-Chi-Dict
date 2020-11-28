from web_chi_dict import WordICiBa, WordYouDao

word = WordICiBa('hot')
print(word.word)  # hot
# print(word.json)  # Full json response
print(word['exchange']['word_third'][0])  # Gets from json
word.speak(types=('us', 'uk'))  # Speak, types: tuple of priority: 'us' for USA, 'uk' for UK, 'tts' for Text-to-Speak

word = WordYouDao('hot')
print(word['basic']['explains'])  # Gets from json
word.speak(threaded=False)
