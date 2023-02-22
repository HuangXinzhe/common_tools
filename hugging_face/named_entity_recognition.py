from transformers import pipeline

ner = pipeline("ner", grouped_entities=True, model="StanfordAIMI/stanford-deidentifier-base")
answer = ner("My name is Sylvain and I work at Hugging Face in Brooklyn.")
print(answer)
