from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

def load_model():
    model_name = "textattack/bert-base-uncased-ag-news"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    model.eval()
    return model, tokenizer

def predict(texts, model, tokenizer):
    inputs = tokenizer(
        texts,
        padding=True,
        truncation=True,
        return_tensors="pt"
    )

    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.argmax(outputs.logits, dim=1)

    return predictions.tolist()
