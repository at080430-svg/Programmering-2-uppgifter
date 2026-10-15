import os

if os.getenv("OPENAI_API_KEY"):
    print("API-nyckeln hittades!")
else:
    print("API-nyckeln hittades inte.")