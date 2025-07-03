ESCALATION_KEYWORDS = ["refund", "payment", "billing", "broken", "damage", "complaint","maintenance"]

def needs_escalation(query: str) -> bool:
    return any(word in query.lower() for word in ESCALATION_KEYWORDS)
