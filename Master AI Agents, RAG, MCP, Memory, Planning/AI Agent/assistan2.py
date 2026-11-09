# Storing history of messages

from openai import OpenAI
from dotenv import load_dotenv
import os 

# Load configuration
load_dotenv()

# AI client 
client = OpenAI(
  base_url=os.getenv("BASE_URL"),
  api_key=os.getenv("API_KEY")
)

print("=" * 40)
print(".  My AI Assistant")
print("=" * 40)
messages = []



while True:
    user_input = input("\nYou:")
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    if user_input.lower() == "quit":
        print("\nAI: Goodbye! Have a great day.")
        break

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages
    )
    messages.append(
        {
            "role": "assistant",
            "content": response.choices[0].message.content
        }
    )
    print("\nAI :",
          response.choices[0].message.content)