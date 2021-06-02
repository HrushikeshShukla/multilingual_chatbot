# importing  dependencies
import re
import inltk
import nltk
nltk.download('punkt')
import io
import random
import string
import warnings
warnings.filterwarnings('ignore')
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from googlesearch import search

##Setting up marathi stopwords
lang='mr'
f=open("marathi_corpus/stop_marathi.txt",'r')
stop_words=f.readlines()
stm=[]
for i in stop_words:
  i.strip()
  stm.append(re.sub('\n',"",i))
f.close()

#reading corpus
f=open('marathi_corpus/covid.txt')
raw=f.read()
f.close()
sent_tokens=nltk.sent_tokenize(raw)
word_tokens=nltk.word_tokenize(raw)

#text preprocessing:
remove_punct_dict=dict((ord(punct),None) for punct in string.punctuation)#removing punctuation
def preprocess(text):
  return (nltk.word_tokenize(text.translate(remove_punct_dict))) #working on word tokens

##greetings
greeting_inputs=("नमस्कार","हाय")
greeting_res=("नमस्कार","हाय")
def greet_sent(sentence):
  for word in sentence.split():
    if word in greeting_inputs:
      return random.choice(greeting_res)

thank_list=['आभार', 'धन्यवाद', 'बाय', "खूप खूप धन्यवाद"]
def bye(sentence):
    for word in sentence.split():
        if word in thank_list:
            return random.choice(thank_list)

#return from knowledge base
def response(user_response):
  bot_response=''
  sent_tokens.append(user_response)
  tfvec=TfidfVectorizer(tokenizer=preprocess,stop_words=stm)
  tfidf=tfvec.fit_transform(sent_tokens)
  vals=cosine_similarity(tfidf[-1],tfidf)
  idx=vals.argsort()[0][-2]
  flat=vals.flatten()
  flat.sort()
  sent_tokens.pop()
  req_tfidf=flat[-2]
  if (req_tfidf==0):
    bot_response=bot_response+"मला माफ करा. मला कळलं नाही तुम्हाला काय म्हणायचंय ते."
    bot_response=bot_response+"\nमला हे इंटरनेटवर मिळाले:"
    query=user_response
    for url in search(query, lang=lang, num_results=3):
      bot_response=bot_response+"\n"+url
    return bot_response
  else:
    bot_response=bot_response+sent_tokens[idx]
    return bot_response

#chating system
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
