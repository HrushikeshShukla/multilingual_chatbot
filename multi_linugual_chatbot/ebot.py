#importing the libraries
import nltk 
import io
import random
import string
import warnings
warnings.filterwarnings('ignore')
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer
from googlesearch import search
lang='en'

#Nltk downloading only for first run
#nltk.download('wordnet')
#nltk.download('punkt')

#reading corpus
f=open('english_corpus/covid.txt')
raw=f.read()
raw=raw.lower()
f.close()
sent_tokens=nltk.sent_tokenize(raw)
word_tokens=nltk.word_tokenize(raw)

#text preprocessing
lemmer=nltk.stem.WordNetLemmatizer()
def lemtokens(tokens):
  return [lemmer.lemmatize(token) for token in tokens] #lemmatizing the tokens
remove_punct_dict=dict((ord(punct),None) for punct in string.punctuation)#remove punctuation
def Lemnormalize(text):
  return lemtokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict))) 

#making greeating
greeting_inputs = ("hello", "hi","hiii","hii","hiiii","hiiii", "greetings", "sup", "what's up","hey")
greeting_res = ["hi", "hey", "hii there", "hi there", "hello", "I am glad! You are talking to me"]
def greet_sent(sentence):
  for word in sentence.split():
    if word.lower() in greeting_inputs:
      return random.choice(greeting_res)

#saying bye and leaving:
thank_response = ('Bye! take care..', 'Bye', 'thanks', 'thanks a lot', 'thank you', 'You are welcome..')
thank_input = ('bye', 'thanks', 'thanks a lot', 'thank you')
def bye(sentence):
  for word in sentence.split():
    if word.lower() in thank_input:
      return random.choice(thank_response)

#return from corpus
def response(user_response):
  bot_response=''
  sent_tokens.append(user_response)
  tfvec=TfidfVectorizer(tokenizer=Lemnormalize,stop_words='english')
  tfidf=tfvec.fit_transform(sent_tokens)
  vals=cosine_similarity(tfidf[-1],tfidf)
  idx=vals.argsort()[0][-2]
  flat=vals.flatten()
  flat.sort()
  req_tfidf=flat[-2]
  sent_tokens.pop()
  if (req_tfidf==0):
    bot_response=bot_response+"I am Sorry. I did not understand\n"
    bot_response=bot_response+"However, I found this on internet:"
    query=user_response
    for url in search(query, lang=lang, num_results=3):
      bot_response=bot_response+"\n"+url
    return bot_response
  else:
    bot_response=bot_response+sent_tokens[idx]
    return bot_response

#chatting system
def chat(user_response):
    bot_response=''
    if bye(user_response)!=None:
        bot_response=bot_response+bye(user_response)
        return (bot_response, False)
    elif greet_sent(user_response)!=None:
        bot_response=bot_response+greet_sent(user_response)
        return (bot_response, True)
    else:
        bot_response=bot_response+response(user_response)
        return(bot_response, True)