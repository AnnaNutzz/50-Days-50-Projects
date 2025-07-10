from transformers import MarianMTModel, MarianTokenizer

model_name = 'Helsinki-NLP/opus-mt-en-hi'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_en_to_hi(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    tgt_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return tgt_text

# Get input from user
english_text = input("Enter English text to translate to Hindi: ")

hindi_translation = translate_en_to_hi(english_text)
print(f"Hindi Translation: {hindi_translation}")
