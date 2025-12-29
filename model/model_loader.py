from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

def load_model():
    model_name = "textattack/distilbert-base-uncased-ag-news"
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Loading model: {model_name} on device: {device}")

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    model.to(device)
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
