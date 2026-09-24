from transformers import MarianMTModel, MarianTokenizer

# Specify the local path where you downloaded the model
model_path = "opus-mt-nl-en"
tokenizer = MarianTokenizer.from_pretrained(model_path)
model = MarianMTModel.from_pretrained(model_path)

def translate_text(text: str) -> str:
    inputs = tokenizer.encode(text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=512, num_beams=4, early_stopping=True)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translated_text

# Test the translation
dutch_text = "Hallo, hoe gaat het met je?"
english_text = translate_text(dutch_text)
print("Translated Text:", english_text)
