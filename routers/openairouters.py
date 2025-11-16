from openai import OpenAI
client = OpenAI()       
response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that helps people find code snippets in a codebase."},
        {"role": "user", "content": "Please complete the code in the middle given the prefix code snippet and suffix code snippet",}    
        ],
    temperature=0.7,
    max_tokens=800,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)
print(response.choices[0].message.content) 