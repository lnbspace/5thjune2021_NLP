# this is a basic testing for NLP
# it helps to test sentiments in the text
# it removes stopwords and works on keywords those are either positive, negative or neutral
from textblob import TextBlob

f1= 'i am very happy now a days' # feedback of a person to text its sentiments

b1= TextBlob(f1) # prepare a blob object
print(b1)
print(b1.sentiment)#,b1.noun_phrases) # gives two parameters output

# polarity is the actual content sentiment it can be in positive, negative floating numbers
# second parameter is subjectivity to tell irrelevance in the text

