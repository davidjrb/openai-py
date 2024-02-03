import yaml
import openai

# Load the configuration from the YAML file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Extract the API key and other settings
api_key = config['openai']['api_key']
model = config['openai']['model']
temperature = config['openai'].get('temperature', 0.7)  # Default to 0.7 if not specified
max_tokens = config['openai'].get('max_tokens', 150)  # Default to 150 if not specified

# Initialize the OpenAI API client
openai.api_key = api_key

# Function to send a message to the API and get the response
def chat_with_openai(prompt):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are ChatGPT, a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message['content']

# Example usage
if __name__ == "__main__":
    user_input = input("Enter your message: ")
    response = chat_with_openai(user_input)
    print("Response:", response)
