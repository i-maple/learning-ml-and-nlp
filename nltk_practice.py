# NLTK is used to create tokens for nlp

import nltk

nltk.download('punkt')
from nltk.tokenize import word_tokenize

sen = 'Hello there, my name is Nishant Pokhrle'

tokens = word_tokenize(sen)
print(tokens)
