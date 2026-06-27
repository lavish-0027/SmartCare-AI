from transformers import pipeline
from intent_classifier import detect_intent
from metrics import metrics

# ==========================
# Load LLM (HuggingFace)
# ==========================
llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=200
)

CONFIDENCE_THRESHOLD = 0.15  # 🔥 NEW


def build_prompt(query, context):
    return f"""
You are SmartCare AI, a polite and professional healthcare assistant.

Rules:
- Answer ONLY using the context below
- Use simple, clear medical language
- Respond in 2–4 sentences
- If information is missing, say so politely
- Maintain a caring and professional tone

Context:
{context}

Question:
{query}

Answer:
"""


def generate_answer(query, retrieved_chunks, similarity_scores):
    metrics.requests += 1
    intent = detect_intent(query.lower())

    # ==========================
    # GREETING HANDLING
    # ==========================
    if intent == "greeting":
        return (
            "🌿 **Welcome to SmartCare AI!** 🤖\n\n"
            "I’m your virtual assistant. I can help you with doctors, services, "
            "appointments, symptoms, and clinic information.\n\n"
            "How may I assist you today?"
        )

    # ==========================
    # CONFIDENCE CHECK
    # ==========================
    max_score = max(similarity_scores)

    if max_score < CONFIDENCE_THRESHOLD:
        metrics.fallbacks += 1
        return (
            "🌿 I’m sorry, I couldn’t find this information in our records.\n"
            "Please contact SmartCare AI support or your clinic for accurate assistance."
        )

    # ==========================
    # BUILD CONTEXT
    # ==========================
    context = "\n".join(chunk["text"] for chunk in retrieved_chunks[:2])
    prompt = build_prompt(query, context)

    # ==========================
    # GENERATE ANSWER
    # ==========================
    response = llm(prompt)[0]["generated_text"].strip()

    # ==========================
    # SAFETY CLEANUP
    # ==========================
    if len(response) < 20:
        metrics.fallbacks += 1
        return (
            "🌿 I’m unable to provide a complete answer based on the available information.\n"
            "Please reach out to your clinic's front desk or SmartCare AI support for help."
        )

    return response
