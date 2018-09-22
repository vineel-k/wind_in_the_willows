###########
# Solution, homework 1
#
# Name and EID: Vineel Kodikanti vk5276
# Option chosen: A
###
import nltk

witwfile = open('windinthewillows.txt',"r")
witw = witwfile.read()
#The tokenizer adds some identification information at the first index 
#In this example it was '\xef\xbb\...'
#There is also a sequence repeated within the sentences after tokenization
#In this example itsays '\r\n so this means that escape sequences were captured
witw_sent = nltk.sent_tokenize(witw)

#Differences:
#There are no escape sequences
#Punctuation is treated as words
witw_words = nltk.word_tokenize(witw)

print(witw_words)



