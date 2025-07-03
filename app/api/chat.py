from fastapi import APIRouter
from app.models.schema import Query, Response
from app.core.retriever import retrieve_answer
from app.core.llm import generate_response
from app.core.escalation import needs_escalation

router = APIRouter()

@router.post("/ask", response_model=Response)
async def ask_bot(query: Query):
    if needs_escalation(query.question):
        return {"response": "This seems to require human assistance. I'll escalate this to our support team."}
    
    answer = retrieve_answer(query.question)
    if answer:
        response = generate_response(query.question, answer)
        return {"response": response}
    else:
        return {"response": "Sorry, I couldn't find an answer. Escalating to support."}
