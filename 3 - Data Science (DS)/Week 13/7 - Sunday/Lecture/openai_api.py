from openai import OpenAI
import os

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_model():
    messages = [{"role": "system", "content": "You are a helpful assistant that always approaches assisting like a Data Science professor."}]

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'q']:
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )

        assistant_response = response.choices[0].message.content
        print(f"Assistant: {assistant_response}")

        messages.append({"role": "assistant", "content": assistant_response})

if __name__ == "__main__":
    chat_with_model()
