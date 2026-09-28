import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

client = Hindsight(
    base_url=os.environ["HINDSIGHT_BASE_URL"],
    api_key=os.environ["HINDSIGHT_API_KEY"],
)

BANK = "test-bank"

client.retain(bank_id=BANK, content="Riya is a conservative investor with a 5-year horizon and avoids high debt.")
print("Retained.")

result = client.recall(bank_id=BANK, query="What is Riya's risk profile?")
for m in result.results:
    print(m.text)

answer = client.reflect(bank_id=BANK, query="How should I approach investment advice for Riya?")
print(answer.text)