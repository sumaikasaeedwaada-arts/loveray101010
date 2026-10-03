
from google import genai

client = genai.Client()

print("🤖 Gemini AI Chatbot")
print("Type 'exit' to stop")

while True:
    message = input("You: ")

    if message.lower() == "exit":
        print("Bot: Bye!")
        break

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=message
    )

    print("Bot:", response.text)