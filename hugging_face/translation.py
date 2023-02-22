from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
answer = translator("Ce cours est produit par Hugging Face.")
print(answer)
