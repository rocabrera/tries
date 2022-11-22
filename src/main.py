from trie import Trie
from loaders import get_meaning
import json

# Load Trie
with open("../data/engmix.txt", "r") as f:
    data = f.read().splitlines()

trie = Trie()

for word in data:
    trie.insert(word)


# Menu
MENU_TEXT = """
-------------------------------------------------------
Correct your text or search for the meaning of a word:
1 - Search meaning.
2 - Correct text.
0 - Exit.
-------------------------------------------------------
"""

def search_meaning(word):
    word_to_be_found = trie.find_with_correction(word.lower())
    ANSWER_MEANING = f"""
--ANSWER--
    Did you mean: {word_to_be_found}?

    Meaning:
    {get_meaning(word_to_be_found)}
    """
    print(ANSWER_MEANING)


def correct_text(text):
    corrected_words = []
    for word in text.split():
        corrected_words.append(trie.find_with_correction(word.lower()))
    correct_text = " ".join(corrected_words)
    ANSWER_CORRECT_TEXT = f"""
--ANSWER--
    Here is your corrected text:

    {correct_text}
    """
    print(ANSWER_CORRECT_TEXT)

print(MENU_TEXT)
choice = input()

while choice != 0:
    if int(choice) == 1:
        print("Now enter the word you want to discover the meaning:")
        word = input()
        search_meaning(word)
        print(MENU_TEXT)
        choice = input()
    elif int(choice) == 2:
        print("Now enter the text you want to be corrected:")
        text = input()
        correct_text(text)
        print(MENU_TEXT)
        choice = input()
    elif int(choice) != 0:
        print("Invalid choice, try again.")
        print(MENU_TEXT)
        choice = input()
    else:
        print("Bye.")
        break