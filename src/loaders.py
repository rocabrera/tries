import json
import os

from src.trie import Trie
from pathlib import Path

DATA_FOLDER = Path(__file__).parent.parent / "data"


def load_file_trie(trie: Trie, dataset: Path):
    """Insert words from a file in a Trie Structure

    Args:
        trie: A Trie structure
        dataset: Path to txt file
    """

    with open(dataset) as f:
        while True:

            line = f.readline().rstrip('\n')
            if not line:
                break
            else:
                trie.insert(line)

def load_data_trie(trie: Trie, dataset: Path):
    """Insert words from files in a Trie Structure

    Args:
        trie: A Trie structure
        dataset: Path to folder which contains txt files
    """

    if dataset.is_dir():
        files = Path(dataset).glob('*')
        for file in files:
            load_file_trie(trie, file)

def get_meaning(word: str):
    """Get the meaning of a word over indexed files
    that are one dictionary of english words

    Args:
        word: The word that will be consulted.
    """

    first_letter = word[0]
    path_to_db = os.environ.get("AED_DICT_DB_PATH", DATA_FOLDER/"dictionary")
    dict_file = open(os.path.join(path_to_db, f"{first_letter}.json"))
    dictionary_from_fletter = json.load(dict_file)
    meaning = dictionary_from_fletter.get(word)

    return meaning
