import json

f = open("../data/dictionary/dictionary_alpha_arrays_original.json", 'r')
dic = json.load(f)

l = 97
for letter in dic:
    with open(f"../data/dictionary/{chr(l)}.json", "w") as f:
        f.writelines(json.dumps(letter))
    l = l+1