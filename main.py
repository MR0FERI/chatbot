import re

def get_response(user_input):
  split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
  response = check_all_message(split_message)
  return response

def message_probability(user_message, recognized_word, single_response=False, required_word=[]):
  message_certainty = 0
  has_required_words = True
  
  for word in user_message:
    if word in recognized_word:
      message_certainty +=1
      
  percentage = float(message_certainty) / float (len(recognized_word))
  
  
while True:
  print("Bot: " + get_response(input('You: ')))
