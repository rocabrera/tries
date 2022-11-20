from src.trie import Trie

with open("data/engmix.txt", "r") as f:
    data = f.read().splitlines()

trie = Trie()

for word in data:
    trie.insert(word)
    
phrase = "richxst man in humyn hixtory".lower()
new_words = []

for word in phrase.split():
    new_words.append(trie.find_with_correction(word))
    
print(" ".join(new_words))