from dotenv import load_dotenv
load_dotenv()  # load environmnt variables from .env
#inpe
import os
import textwrap

import google.generativeai as genai
from IPython.display import Markdown

# configure google genAI API
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function_to_load_open_ai_model_and_get_response
def get_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# interaction with user
print("welcome to  Q/A Chatbot")


while True:
    user_input = input("enter your query (TO END CONVERSATION please type 'exit' to end): ")
    
    if user_input.lower() == 'exit':
        break

    response = get_response(user_input)

    print("\nSimran's_chat_bot's Response:")
    print(response)
    print("\n" + "=" * 50 + "\n")
