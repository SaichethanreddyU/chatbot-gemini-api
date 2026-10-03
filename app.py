from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

chat = client.chats.create(
    model="gemini-3.8-flash",
    config={
        "system_instruction": "You are a helpful and friendly chatbot. "
                              "Explain technical topics simply."
    }
)

print("=" * 50)
print("🤖 My Chatbot")
print("Type /help to see commands")
print("=" * 50)


while True:

    user_input = input("\nYou: ").strip()

    # Exit
    if user_input.lower() == "/exit":
        print("Bot: Goodbye!")
        break

    # Help
    elif user_input.lower() == "/help":
        print("""
Commands:
  /help     Show commands
  /clear    Clear conversation
  /history  Show conversation history
  /exit     Exit chatbot
""")
        continue

    # Clear conversation
    elif user_input.lower() == "/clear":
        chat = client.chats.create(
            model="gemini-3.8-flash",
            config={
                "system_instruction":
                    "You are a helpful and friendly chatbot. "
                    "Explain technical topics simply."
            }
        )

        print("Bot: Conversation cleared.")
        continue

    # History
    elif user_input.lower() == "/history":
        history = chat.get_history()

        print("\n--- Conversation History ---")

        for message in history:
            print(message)

        print("----------------------------")
        continue

    # Empty input
    elif not user_input:
        print("Bot: Please enter a message.")
        continue

    # Send message
    try:
        print("Bot: ", end="", flush=True)

        response = chat.send_message(user_input)

        print(response.text)

    except Exception as e:
        print("\nError:", e)