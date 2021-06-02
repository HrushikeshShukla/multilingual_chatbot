lang=['en','mr'] #defining the languages
from mbot import chat as mre
from ebot import chat as ere

class chatbot:
  def __init__(self,x):
    if x==1:
      self.chat=mre
    else:
      self.chat=ere
  def reply(self,user_input):
    self.response=self.chat(user_input)
    return(self.response)