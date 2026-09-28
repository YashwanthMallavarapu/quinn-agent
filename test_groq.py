import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

llm = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=os.environ["GROQ_API_KEY"])

resp = llm.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "user", "content": "Explain debt-to-equity ratio in two sentences."}],
)
print(resp.choices[0].message.content)