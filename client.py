import openai

# Set your API key
openai.api_key = "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"

# Create a completion
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud."},
        {"role": "user", "content": "What is coding?"}
    ]
)

# Print the response
print(completion['choices'][0]['message']['content'])
