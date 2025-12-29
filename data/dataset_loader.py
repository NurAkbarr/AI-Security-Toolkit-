from datasets import load_dataset

def load_data(limit=100):
    dataset = load_dataset("ag_news", split=f"test[:{limit}]")

    texts = [str(t) for t in dataset["text"]]
    labels = dataset["label"]

    return texts, labels
