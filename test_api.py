
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Svara med exakt text: API fungerar!"
)

print(response.output_text)