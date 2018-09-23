###########
# Solution, homework 1
#
# Name and EID: Vineel Kodikanti vk5276
# Option chosen: A
###
import nltk
import string


#Open and save file as string 
with  open('windinthewillows.txt',"r",encoding = 'utf_8', errors = 'ignore') as witwfile:
    witw = witwfile.read()

#Tokenize Sentences
#The tokenizer adds some identification information at the first index 
#In this example it was '\xef\xbb\...'
#There is also a sequence repeated within the sentences after tokenization
#In this example itsays '\r\n so this means that escape sequences were captured
witw_sent = nltk.sent_tokenize(witw)

#Differences:
#There are no escape sequences
#Punctuation is treated as words
witw_words = nltk.word_tokenize(witw)

#Stopwords
# the contents of the stop variable is a list which contains preprositions 
# these prepositions may not aid in understand of sentence because many of them are related to possesion, linkage, etc. 

stop =  nltk.corpus.stopwords.words("english")

#remove stopwords from witw_words
witw_goodwords = [i for i in witw_words if i  not in stop]

#remove punctuation
witw_goodwords_nopunct = [i for i in witw_words if i not in string.punctuation]

#POS tagging
#witw_wtags2 has more erros
# some errors include labling struck as a noun in the phrase the sunshine struck hot on his fur in both lists
# Onion-sauce is labled as a noun in witw-wtags in the first list but was JJ in the second list
#created a list of all the differences between both lists below
witw_wtags =  nltk.pos_tag(witw_words)
witw_wtags2 = nltk.pos_tag(witw_goodwords_nopunct)
differences = [i for i in witw_wtags if i not in witw_wtags2]

# extract nouns

witw_nouns = [i for i in witw_wtags if i[1] == 'NN' ]

