import pytest
import random
from time import time
from src.loaders import load_data_trie, load_file_trie
from pathlib import Path
from src.trie import Trie

random.seed(42)

DATA_PATH = Path(__file__).parent.parent

@pytest.fixture(params=[
    ["testtes", "test", "testte"], 
    ["test", "testte", "testtes"], 
    ["testte", "test", "testtes"]
])
def trie_with_suffix(request):
    """
    Same tries with different insert order
    """
    
    trie = Trie()

    for word in request.param:
        trie.insert(word)

    return trie

@pytest.fixture(params=[
    ["amor", "aamor", "aammor"], 
    ["aamor", "amor", "aammor"], 
    ["aammor", "aamor", "amor"]
])
def trie_with_prefix(request):
    """
    Same tries with different insert order
    """
    
    trie = Trie()

    for word in request.param:
        trie.insert(word)

    return trie

@pytest.fixture()
def full_trie_with_execution_time():

    trie = Trie()
    data_folder = Path(__file__).parent.parent / "data"

    start = time()
    load_data_trie(
        trie = trie,
        dataset = data_folder / "words_splitted"
    )
    end = time()
    execution_time = end - start

    return trie, execution_time

@pytest.fixture()
def smaller_trie_with_execution_time():

    trie = Trie()
    data_folder = Path(__file__).parent.parent / "data"

    start = time()
    load_file_trie(
        trie = trie,
        dataset = data_folder / "engmix.txt"
    )
    end = time()
    execution_time = end - start

    return trie, execution_time

@pytest.fixture(params=[100, 1000, 10000])
def indexs_smaller_file(request):

    list_of_idxs = random.sample(range(0, 84100), request.param)

    return  list_of_idxs