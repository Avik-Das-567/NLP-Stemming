import streamlit as st
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

text = "I am enjoying, enjoyed, and enjoys this moment."

words = word_tokenize(text)
stemmed = [ps.stem(w) for w in words]

print("Stemmed:", stemmed)