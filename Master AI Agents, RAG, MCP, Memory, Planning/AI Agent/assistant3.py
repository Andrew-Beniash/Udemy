# Adding system role

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

# Roles
roles = {
    "1": "You are a friendly school teacher. Always provide a single sentence response",
    "2": "You are a senior Python developer. Explain programming concepts clearly and concisely.",
    "3": "You are experience travel guide.",
    "4": "You are motivational coach.",
    "5": "You are professional interviewer."
}

print("=" * 40)
print(".  My AI Assistant")
print("=" * 40)

print("\nChoose Your Asssistant Role:")

print("\n1. Friendly School Teacher")
print("\n2. Senior Python Developer")
print("\n3. Travel Guide")
print("\n4. Motivational Coach")
print("\n5. Interviewer")

choice=input("\n Enter your choice: ")

messages = [
    {
        "role":"system",
        "content": roles.get(choice, "You are helpful AI assistant")
    }
]



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