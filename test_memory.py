import time
import memory

USER = "riya-test"

print("Retaining...")
memory.remember_profile(USER, "Conservative investor, 5-year horizon, avoids high debt. Watching TCS and Infosys.")
memory.remember_thesis(
    USER, "TCS", "Buy", "Medium", "5 years",
    "operating margin below 22% for two quarters",
    "Strong cash flow and low debt; risk is margin pressure from wage inflation.",
)
memory.remember_feedback(USER, "Always include forex exposure when analyzing IT exporters.")

print("Waiting for Hindsight to process (20s)...")
time.sleep(20)

print("\n--- RECALL: preferences ---")
print(memory.recall_as_text(USER, "What are this user's preferences and risk profile?"))

print("\n--- RECALL: TCS ---")
print(memory.recall_as_text(USER, "What did we conclude about TCS and what are its thesis breakers?"))

print("\n--- Adding an outcome ---")
memory.remember_outcome(USER, "TCS", "Operating margin fell to 21% for two quarters. Thesis breaker triggered, thesis invalidated.")
time.sleep(20)

print("\n--- REFLECT ---")
print(memory.lessons(USER))