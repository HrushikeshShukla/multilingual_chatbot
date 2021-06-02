lang=['en','mr'] #defining the languages

print("***Welcome to multilinugal chatbot.***")
print("***बहुभाषिक ​​चॅटबॉटमध्ये आपले स्वागत आहे.***")
print("\n \nPlease Select language:\nकृपया भाषा निवडा:")
indx=int(input("\nPress 1 for english, मराठीसाठी 2 दाबा: "))

if indx==2:
  from mbot import chat
  print("starting marathi version.")
  print("मराठी आवृत्ती सुरू करीत आहे.")
  flag=True
  print("रोबोट: नमस्कार")
  while flag==True:
    user_response=input("आपण: ")
    bot_response,flag=chat(user_response)
    print("रोबोट: "+str(bot_response))
else:
  from ebot import chat
  print("Starting english version")
  flag=True
  print("Bot: Hello!")
  while flag==True:
    user_response=input("You: ")
    bot_response,flag=chat(user_response)
    print("Bot: "+str(bot_response))

