# textblob is used for sentiment analysis


from textblob import TextBlob

text = TextBlob(input('Enter a string to analyse sentiment'))

sentiment = text.sentiment.polarity

print(sentiment)