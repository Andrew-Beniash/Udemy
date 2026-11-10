# Primitive tool use

from openai import OpenAI
from dotenv import load_dotenv
import os 
from tools import (
    get_current_time,
    roll_dice,
    generate_password
)

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



while True:
    user_input = input("\nYou:")
    text = user_input.lower()

    if "generate" in user_input.lower():
            print("\n AI: ", generate_password())
    
            continue
    
    elif "time" in text or "clock" in text:
        print("\n AI: ", get_current_time())

        continue

    elif "dice" in user_input.lower():
        print("\n AI: You rolled", roll_dice())

        continue

    
    
    elif user_input.lower() == "quit":
        print("\nAI: Goodbye! Have a great day.")
        break

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {"role": "user",
             #"instructions": "Always respond with one sentence only",
             "content": user_input
            }
        ]
    )

    print("\nAI :",
          response.choices[0].message.content)

    