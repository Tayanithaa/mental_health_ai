from transformers import pipeline

# Load Hugging Face model once
pipe = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

def analyze_text(text):
    results = pipe(text)[0]  # list of dicts with label + score
    scores = {res["label"].lower(): res["score"] for res in results}
    # Pick top emotion
    emotion = max(scores, key=scores.get)
    return emotion, scores
