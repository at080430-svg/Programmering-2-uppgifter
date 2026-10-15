
from openai import OpenAI

client = OpenAI()

modeller = client.models.list()

sokord = ["davinci", "gpt-3.5", "gpt-4o", "gpt-5", "gpt-6"]

for modell in modeller:
    if any(ord in modell.id.lower() for ord in sokord):
        print(modell.id)    