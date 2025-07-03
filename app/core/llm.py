import google.generativeai as genai
from app.core.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
def generate_response(user_query: str, retrieved_answer: str) -> str:
    model = genai.GenerativeModel("gemini-2.0-flash")  # or "gemini-pro"

    prompt = f"""
Guest question: "{user_query}"

Answer: "{retrieved_answer}"

Just make the answer sound slightly more friendly and polite. Do not expand it. Keep it short and simple.
"""

    response = model.generate_content(prompt)

    return response.text.strip()