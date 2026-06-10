import json


def load_input(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_output(path, data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
