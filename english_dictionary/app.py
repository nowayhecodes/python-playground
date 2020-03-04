from difflib import get_close_matches
import json

data = json.load(open("definitions.json"))


def search(term):
    return data[term][0] if term in data else "Term not found"


while True:
    term = input("Search term: ").lower()
    print(f"\n{search(term)}\n")
