import json

def read_json(path): 
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


# document = read_json("vocab.json")
# print(document["JLPT N5 Kanji"][0])