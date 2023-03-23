from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
# max_length或min_length控制翻译长短
answer = translator("Ce cours est produit par Hugging Face.")
print(answer)
