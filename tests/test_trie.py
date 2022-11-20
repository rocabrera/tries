from pathlib import Path
from time import time

def test_trie_find_suffix(trie_with_suffix):
    
    assert trie_with_suffix.find("testtes")[0]
    assert trie_with_suffix.find("test")[0]
    assert trie_with_suffix.find("testte")[0]
    assert not trie_with_suffix.find("tes")[0]
    

def test_trie_find_prefix(trie_with_prefix):
    
    assert trie_with_prefix.find("amor")[0]
    assert trie_with_prefix.find("aamor")[0]
    assert trie_with_prefix.find("aammor")[0]
    assert not trie_with_prefix.find("a")[0]


def test_structure_mean_time_access(full_trie_with_execution_time):
    
    full_trie, _ = full_trie_with_execution_time
    dataset = Path(__file__).parent.parent \
              / "data" \
              / "words_alpha.txt"

    count = 0
    total_find_time = 0  
    total_matches = 0
    with open(dataset) as f:
        while True:
            
            line = f.readline().rstrip('\n')
            if not line:
                break
            else:
                count += 1
                start = time()
                result,_ = full_trie.find(line)
                end = time()
                total_find_time += (end - start)
                total_matches += int(result)

    mean_find_time = total_find_time/count
    assert mean_find_time < 5.0e-06
    assert total_matches == 370105


