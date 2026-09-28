import os
from datetime import date
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

_client = Hindsight(
    base_url=os.environ["HINDSIGHT_BASE_URL"],
    api_key=os.environ["HINDSIGHT_API_KEY"],
    timeout=60.0,
)


def bank_for(user_id: str) -> str:
    """One memory bank per user, so memories never mix."""
    clean = user_id.strip().lower().replace(" ", "-")
    return f"analyst-{clean}"


def _today() -> str:
    return date.today().isoformat()


# ---------- RETAIN ----------

def remember(user_id: str, text: str) -> bool:
    """Store a raw memory. Returns True on success, False on failure."""
    try:
        _client.retain(bank_id=bank_for(user_id), content=text)
        return True
    except Exception as e:
        print(f"[memory] retain failed: {e}")
        return False


def remember_profile(user_id: str, profile_text: str) -> bool:
    return remember(user_id, f"[USER PROFILE, {_today()}] {profile_text}")


def remember_thesis(user_id: str, ticker: str, rating: str, conviction: str,
                    horizon: str, breakers: str, summary: str) -> bool:
    text = (
        f"[THESIS, {_today()}] {ticker}: rating {rating}, conviction {conviction}, "
        f"horizon {horizon}. Thesis breakers: {breakers}. Summary: {summary}"
    )
    return remember(user_id, text)


def remember_feedback(user_id: str, feedback: str) -> bool:
    return remember(user_id, f"[USER FEEDBACK, {_today()}] {feedback}")


def remember_outcome(user_id: str, ticker: str, outcome: str) -> bool:
    return remember(user_id, f"[OUTCOME, {_today()}] {ticker}: {outcome}")


# ---------- RECALL ----------

def recall(user_id: str, query: str, max_items: int = 10) -> list[str]:
    """Return a list of memory strings relevant to the query."""
    try:
        result = _client.recall(bank_id=bank_for(user_id), query=query)
        return [m.text for m in result.results][:max_items]
    except Exception as e:
        print(f"[memory] recall failed: {e}")
        return []


def recall_as_text(user_id: str, query: str, max_items: int = 10) -> str:
    """Recall formatted for pasting into an LLM prompt."""
    items = recall(user_id, query, max_items)
    if not items:
        return "No relevant memories yet."
    return "\n".join(f"- {t}" for t in items)


# ---------- REFLECT ----------

def reflect(user_id: str, query: str) -> str:
    """Ask Hindsight to reason over memories and return lessons."""
    try:
        answer = _client.reflect(bank_id=bank_for(user_id), query=query)
        return answer.text
    except Exception as e:
        print(f"[memory] reflect failed: {e}")
        return "Reflection is unavailable right now."


def lessons(user_id: str) -> str:
    return reflect(
        user_id,
        "What patterns explain which of this user's investment theses worked or failed, "
        "and what do their preferences and corrections imply for future research?",
    )