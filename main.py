from data.dataset_loader import load_data
from model.model_loader import load_model
from attack.text_attack import build_attacker

from textattack.attack_results import SuccessfulAttackResult

def main():
    texts, labels = load_data(limit=20)
    model, tokenizer = load_model()

    attacker = build_attacker(model, tokenizer, texts, labels)

    results = attacker.attack_dataset()

    success = 0
    for result in results:
        if isinstance(result, SuccessfulAttackResult):
            success += 1

    print("Total samples:", len(texts))
    print("Attack succeeded:", success)
    print("Attack success rate:", success / len(results) * 100, "%")

if __name__ == "__main__":
    main()
