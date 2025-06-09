# Stemming in NLP
### App Link
- https://nlp-stemming.streamlit.app/
---
### What is Stemming?
- **Stemming** is the process of cutting words to their **base or root form**.
- It helps group similar words like “playing”, “played”, “plays” into a single base word → “**play**”.
- The stem **may not be a valid word**, but it represents the core meaning.
- **Example Sentence:**

  > "He is playing and she played."
  
  After stemming:
  > "He is play and she play."

  Now both words refer to the same **action**, making analysis easier.
---
### Why Use Stemming?
- To **simplify text** for machine learning.
- Reduces **vocabulary size**.
- Helps in **search engines**, **text classification**, and **sentiment analysis**.
---
### Required Python Packages
- **`nltk`**
- **`streamlit`**
---
### How the App Works -
- **Input:**
```
text = "I am enjoying, enjoyed, and enjoys this moment."
```
- **Output:**
```
Stemmed: ["I", "am", "enjoy", ",", "enjoy", ",", "and", "enjoy", 'thi", "moment", "."]
```
- Words like "enjoying", "enjoyed", "enjoys" are all reduced to "**enjoy**".
---
### Additional Insights :
- Stemming does not always return **real dictionary words**.
- Stemming works based on **rules** and **patterns**.
- Common stemmers: **PorterStemmer**, **SnowballStemmer**, **LancasterStemmer**.
---
