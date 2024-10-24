#!/usr/bin/env python
# coding: utf-8

# Examples of Regular Expressions

# In[1]:


import re


# Analysis of Words

# In[2]:


# Example#1

my_string0 = "Let's write RegEx"


# In[3]:


# The r"" syntax denotes a raw string literal. This means that any escape sequences within the string 
# (like \n, \t, or \\) are treated as literal characters and are not processed by the Python interpreter. 
# This can be particularly useful when dealing with regular expressions, file paths, or any strings where backslashes are common.


# In[4]:


# Find all words
wordToken = r"\w+"

matches = re.findall(wordToken, my_string0)
print(matches)

for match in matches:
  print(match)


# In[5]:


# Example#2

my_string1 = "Let's write RegEx!  Won't that be fun?  I sure think so.  Can you find 4 sentences?  Or perhaps, all 19 words?"


# In[6]:


# Find all capicalized words in my_string and print the result

capitalized_words = r"[A-Z]\w+"
print(re.findall(capitalized_words, my_string1))


# In[7]:


# Function: Print ‘n’ words in a row

def print_words (list_words, numElementsRow):

  for j in range (0, len(list_words), numElementsRow):
    for i in range(j, j + numElementsRow):
      if ( i >= len(list_words)):
        break
      print(i, '.',list_words[i], end=', ')
    print()
  print()


# In[8]:


# Split my_string on spaces and print the result
spaces = r"\s+"

list_of_words = re.split(spaces, my_string1)

# print(re.split(spaces, my_string1))
print_words(list_of_words,5)


# In[9]:


# Find all digits in my_string and print the result

digits = r"\d+"
print(re.findall(digits, my_string1))


# In[10]:


# Example #2
my_string1 = "Let's write RegEx!  Won't that be fun?  I sure think so.  Can you find 4 sentences?  Or perhaps, all 19 words?"


# In[11]:


# 1. Split my_string on sentence endings and print the result

sentence_ending = re.compile(r"[.?!]")

matches = sentence_ending.finditer(my_string1)
for match in matches:
  print(match)


# In[12]:


print(re.split(sentence_ending, my_string1))


# In[13]:


# Example#2

my_string2 = 'The URL of Google is www.google.com'


# In[14]:


# 1. Split my_string on sentence endings and print the result

sentence_ending = re.compile(r"[.?!]")

matches = sentence_ending.finditer(my_string2)
for match in matches:
   print(match)


# In[15]:


print(re.split(sentence_ending, my_string2))


# NLTK Tokenizer

# In[16]:


# from google.colab import files
# f = files.upload()


# In[17]:


get_ipython().system('ls')


# In[18]:


with open('grail.txt', 'r') as file:
    holy_grail = file.read()
    scene_one = re.split('SCENE 2:', holy_grail)[0]

# print(scene_one)


# In[19]:


with open('grail.txt', 'r') as file:
    holy_grail = file.read()
    scene_one = re.split('SCENE 2:', holy_grail)[0]

print(type(scene_one))
print(scene_one)


# In[20]:


import sys
print(sys.executable)


# In[21]:


import nltk
nltk.download('punkt')
nltk.download('punkt_tab')


# In[22]:


from nltk.tokenize import word_tokenize, sent_tokenize


# In[23]:


# Split scene_one into sentences: sentences

sentences = sent_tokenize(scene_one)
print_words(sentences, 1)


# In[24]:


# Use word_tokenize to tokenize the third sentence: tokenized_sent

tokenized_sent = word_tokenize(sentences[2])
print_words(tokenized_sent, 5)


# In[25]:


# Make a set of unique tokens in the entire scene: unique_tokens

unique_tokens = set(word_tokenize(scene_one))
print(unique_tokens)


# In[26]:


# Print the unique tokens result

print_words(list(unique_tokens),5)


# Match Regular Expressions

# In[27]:


match = re.search("coconuts", scene_one)

# Print the start and end indexes of match
print(match.start(), match.end())

print(scene_one[589:597])


# Advanced Tokenization with NLTK and regex

# In[28]:


from pprint import pprint

from nltk.tokenize import regexp_tokenize


# In[36]:


my_string = "SOLDIER #1: Found them? In Mercea? The coconut's tropical!"


# In[40]:


pattern1 = r'(\\w+|\\?|!)'
pattern2 = r"(\w+|#\d|\?|!)"
pattern3 = r'(#\\d\\w+\\?!)'
pattern4 = r'\\s+'


# In[47]:


pprint(regexp_tokenize(my_string, pattern2))


# In[48]:


pprint(regexp_tokenize(my_string, pattern4))


# In[49]:


# 1. Pattern 1: r'(\\w+|\\?|!)'

#  \\w+: This matches one or more alphanumeric characters (letters, digits, and underscores).
#  \\?: This matches a literal question mark (?).
#  !: This matches a literal exclamation mark (!).
#  |: This is an OR operator, so the pattern matches either \\w+ (alphanumeric string), \\? (question mark), or ! (exclamation mark).

# Simplified Explanation: This pattern matches any sequence of alphanumeric characters, or a standalone ? or !.

# 2. Pattern 2: r"(\w+|#\d|\?|!)"

#  \w+: Matches one or more alphanumeric characters.
#  #\d: Matches a literal # followed by a digit.
#  \?: Matches a literal question mark (?).
#  !: Matches a literal exclamation mark (!).
#  |: This OR operator matches any of these options.

# Simplified Explanation: This pattern matches any alphanumeric string, a # followed by a digit, or a standalone ? or !.

# 3. Pattern 3: r'(#\\d\\w+\\?!)'

#  #\\d: Matches a literal # followed by a digit.
#  \\w+: Matches one or more alphanumeric characters.
#  \\?: Matches a literal question mark (?).
#  !: Matches a literal exclamation mark (!).

# Simplified Explanation: This pattern matches strings that start with a # followed by a digit, then a sequence of alphanumeric characters, and ends with a ?!.

# 4. Pattern 4: r'\\s+'

#  \\s+: Matches one or more whitespace characters (spaces, tabs, newlines).

# Simplified Explanation: This pattern matches any sequence of one or more whitespace characters.


# In[54]:


# Three tweets

tweets = ['This is the best #nlp exercise ive found online! #python',
          '#NLP is super fun! <3 #learning',
          'Thanks @chapman :) #nlp #python']


# In[55]:


from nltk.tokenize import regexp_tokenize, TweetTokenizer


# In[56]:


# Define a regex pattern to find hashtags: pattern1
pattern1 = r"#\w+"


# In[57]:


print(tweets[0])


# In[59]:


# Use the pattern on the first tweet in the tweets list

# The use regexp_tokenize() with this pattern, 
# will find and return all the hashtags present in the tweet.

hashtags = regexp_tokenize(tweets[0], pattern1)
print(hashtags)


# In[60]:


pattern2 = r"[@|#]\w+"


# In[61]:


print(tweets[-1])


# In[62]:


# Use the pattern on the last tweet in the tweets list

mentions_hashtags = regexp_tokenize(tweets[-1], pattern2)
print(mentions_hashtags)


# In[63]:


tknzr = TweetTokenizer()
all_tokens = [tknzr.tokenize(t) for t in tweets]
print_words(all_tokens, 1)


# Non-ascii tokenization

# In[64]:


german_text = 'Wann gehen wir Pizza essen? 🍕 Und fährst du mit Über? 🚕'


# In[65]:


all_words = word_tokenize(german_text)
print(all_words)

# Tokenize and print only capital words

capital_words = r"[A-ZÜ]\w+"
print(regexp_tokenize(german_text, capital_words))

# Tokenize and print only emoji

emoji = "['\U0001F300-\U0001F5FF'|'\U0001F600-\U0001F64F'|'\U0001F680-\U0001F6FF'|'\u2600-\u26FF\u2700-\u27BF']"
print(regexp_tokenize(german_text, emoji))


# Charting Word Length with NLTK

# In[67]:


import matplotlib.pyplot as plt

# Split the script into lines: lines
lines = holy_grail.split('\n')

# Replace all script lines for speaker
pattern = "[A-Z]{2,}(\s)?(#\d)?([A-Z]{2,})?:"
lines = [re.sub(pattern, '', l) for l in lines]

# Tokenize each line: tokenized_lines
tokenized_lines = [regexp_tokenize(s, '\w+') for s in lines]

# Make a frequency list of lengths: line_num_words
line_num_words = [len(t_line) for t_line in tokenized_lines]

# Plot a histogram of the line lengths
plt.figure(figsize=(8,8))
plt.hist(line_num_words);
plt.title('# of words per line in holy_grail');


# In[68]:


lines = [re.sub(pattern, '', l) for l in lines]
print(lines)

tokenized_lines = [regexp_tokenize(s, '\w+') for s in lines]
print(tokenized_lines)