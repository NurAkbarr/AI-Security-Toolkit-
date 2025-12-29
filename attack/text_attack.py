import textattack
from textattack.models.wrappers import HuggingFaceModelWrapper
from textattack import Attacker
from textattack.datasets import Dataset

def build_attacker(model, tokenizer, texts, labels):
    model_wrapper = HuggingFaceModelWrapper(model, tokenizer)

    attack = textattack.attack_recipes.TextFoolerJin2019.build(
        model_wrapper
    )

    dataset = Dataset(list(zip(texts, labels)))

    attacker = Attacker(attack, dataset)
    return attacker
