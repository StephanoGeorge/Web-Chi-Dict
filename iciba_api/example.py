from iciba_api import Word

word = Word('hot')
print(word['word_name'])  # hot
print(word['exchange']['word_third'])  # hots
pronounce = word.pronounce()  # get bytes of the pronunciation
word.pronounce('en', True)  # speak
