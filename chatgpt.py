import openai
import os

# Fetch the API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Example API request
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "What is an API?"}
    ]
)

print(response.choices[0].message['content'])
