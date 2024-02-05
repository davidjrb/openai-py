import os
from openai import OpenAI

# Initialize OpenAI client with API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Function to run the chat in terminal
def run_chat():
    while True:
        user_input = input("You: ")  # Get input from the user
        if user_input.lower() == "exit":  # Provide a way to exit the loop
            print("Exiting chat.")
            break

        # Generate response using GPT-4
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": user_input}],
            model="gpt-4",  # Use the correct GPT-4 model identifier
        )

        # Print the model's response
        print("AI:", chat_completion.choices[0].message.content)

# Run the chat function
if __name__ == "__main__":
    run_chat()
