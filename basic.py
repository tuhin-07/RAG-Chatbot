from transformers import AutoTokenizer

# Load the tokenizer for LLaMA 3 (or any other model)
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")

# Your input text
text = "How many tokens are in this sentence?"

# Tokenize the input
tokens = tokenizer(text, return_tensors="pt")

# Get the number of tokens
num_tokens = tokens["input_ids"].shape[1]

print(f"Number of tokens: {num_tokens}")
print(tokenizer.tokenize(text))         # List of string tokens
print(tokenizer.convert_ids_to_tokens(tokens["input_ids"][0]))  # Tokens with IDs
