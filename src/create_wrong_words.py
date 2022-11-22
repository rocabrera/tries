import random
from pathlib import Path
from string import ascii_lowercase


DATA_FOLDER = Path(".").parent.parent / "data"


def create_dataset_with_wrong_letter(dataset_path: str):
    
    with open(DATA_FOLDER / "files_with_errors" / f"wrongs_{dataset_path}", "w") as write_f:
        
        with open(DATA_FOLDER / dataset_path, "r") as read_f:
            while True:

                word = read_f.readline().rstrip('\n')
                if not word:
                    break
                else:
                    old_letter = random.sample(word, 1)[0]
                    new_letter = random.sample(ascii_lowercase.replace(old_letter, ""), 1)[0]

                    idx_old_letter = word.index(old_letter)

                    new_word = word[:idx_old_letter] + new_letter + word[idx_old_letter+1:]
                    
                    write_f.write(new_word+"\n")



if __name__ == '__main__':
    larger_dataset = "words_alpha.txt"
    print(f"Creating larger dataset: {larger_dataset}")
    create_dataset_with_wrong_letter(larger_dataset)
    print(f"Done: {larger_dataset}")

    smaller_dataset = "engmix.txt"
    print(f"Creating larger dataset: {smaller_dataset}")
    create_dataset_with_wrong_letter(smaller_dataset)
    print(f"Done: {smaller_dataset}")

    