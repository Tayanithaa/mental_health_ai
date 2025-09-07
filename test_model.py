from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

text = "I feel really stressed today but I’m hopeful things will get better."
result = sentiment_pipeline(text)

print("Input:", text)
print("Result:", result)
