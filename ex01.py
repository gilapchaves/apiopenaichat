import openai

def acesso():
    openai.api_key = ""
    return openai.api_key

key = acesso()

key = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Tell me about Atlantis in one paragraph."}]
)

print(key)