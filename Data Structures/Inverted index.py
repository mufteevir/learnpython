# return the list of lines in which the word is present

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

# this will open the file
file = open('file.txt', encoding='utf8')  # Open: It is used to open the file.
read = file.read()  # read: This function is used to read the content of the file.
file.seek(0)  # seek(0): It returns the cursor to the beginning of the file.
print(read)

# to obtain the number of lines in file
line = 1
for word in read:
    if word == '\n':
        line += 1

# create a list to store each line as an element of list
array = []
for i in range(line):
    array.append(file.readline())

# Remove punctuation
punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
for ele in read:
    if ele in punc:
        read = read.replace(ele, " ")

# to maintain uniformity
read = read.lower()

# Clean data by removing stopwords:
# Stop words are those words that have no emotions associated
# with it and can safely be ignored without sacrificing the meaning of the sentence.
# this will convert
# the word into tokens
text_tokens = word_tokenize(read)
tokens_without_sw = set([word for word in text_tokens if not word in stopwords.words()])

# Create an inverted index
dict = {}
for i in range(line):
    check = array[i].lower()
    for item in tokens_without_sw:
        if item in check:
            if item not in dict:
                dict[item] = []
            if item in dict:
                dict[item].append(i + 1)
print(dict)
