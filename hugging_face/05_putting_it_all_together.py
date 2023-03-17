from transformers import AutoTokenizer

checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

"""
可以一次标记单个序列，也可以一次标记多个序列
"""
# sequence = "I've been waiting for a HuggingFace course my whole life."
sequences = ["I've been waiting for a HuggingFace course my whole life.", "So have I!"]

model_inputs = tokenizer(sequences)

"""
以下是几种不同的padding方式
"""
# Will pad the sequences up to the maximum sequence length
model_inputs = tokenizer(sequences, padding="longest")

# Will pad the sequences up to the model max length   (512 for BERT or DistilBERT)
# model_inputs = tokenizer(sequences, padding="max_length")

# Will pad the sequences up to the specified max length
# model_inputs = tokenizer(sequences, padding="max_length", max_length=8)

"""
截短序列
"""
# sequences = ["I've been waiting for a HuggingFace course my whole life.", "So have I!"]

# Will truncate the sequences that are longer than the model max length   (512 for BERT or DistilBERT)
# model_inputs = tokenizer(sequences, truncation=True)

# Will truncate the sequences that are longer than the specified max length
# model_inputs = tokenizer(sequences, max_length=8, truncation=True)



sequences = ["I've been waiting for a HuggingFace course my whole life.", "So have I!"]

# Returns PyTorch tensors
model_inputs = tokenizer(sequences, padding=True, return_tensors="pt")

# Returns TensorFlow tensors
model_inputs = tokenizer(sequences, padding=True, return_tensors="tf")

# Returns NumPy arrays
model_inputs = tokenizer(sequences, padding=True, return_tensors="np")