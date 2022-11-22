import pytest
from time import time
from pathlib import Path


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

# def test_performance_larger_file(full_trie_with_execution_time):

#     full_trie, _ = full_trie_with_execution_time

#     correct_dataset = Path(__file__).parent.parent \
#               / "data" \
#               / "words_alpha.txt"

#     wrong_dataset = Path(__file__).parent.parent \
#               / "data" \
#               / "files_with_errors" \
#               / "wrongs_words_alpha.txt"

#     correct_matches = 0
#     counter = 0
#     start = time()

#     with open(correct_dataset) as correct_f:
#         with open(wrong_dataset) as wrong_f:
#             while True:
                
#                 correct_word = correct_f.readline().rstrip('\n')
#                 wrong_word = wrong_f.readline().rstrip('\n')
                
#                 if not correct_word:
#                     break
#                 else:
#                     result = full_trie.find_with_correction(wrong_word)
                    
#                     correct_matches += int(result == correct_word)
#                 if counter%10000 == 0:
#                     print(counter)
#                 counter += 1

#     end = time()
    
#     print(start - end)
#     print(correct_matches/full_trie.n_words)

@pytest.mark.parametrize("maximum_explore", [50,100,150,200])
def test_performance_smaller_file(smaller_trie_with_execution_time, indexs_smaller_file, maximum_explore):

    small_trie, _ = smaller_trie_with_execution_time
    
    correct_dataset = Path(__file__).parent.parent \
              / "data" \
              / "engmix.txt"

    wrong_dataset = Path(__file__).parent.parent \
              / "data" \
              / "files_with_errors" \
              / "wrongs_engmix.txt"

    correct_matches = 0
    counter = 0
    
    count_positon_file = 0

    with open(correct_dataset) as correct_f:
        with open(wrong_dataset) as wrong_f:
            while True:
            
                correct_word = correct_f.readline().rstrip('\n')
                wrong_word = wrong_f.readline().rstrip('\n')
                
                if not correct_word:
                    break
                if count_positon_file in indexs_smaller_file:
                    result = small_trie.find_with_correction(wrong_word, maximum_explore)
                    correct_matches += int(result == correct_word)
                
                counter += 1
                count_positon_file += 1 

    print(f"Número de palavras a serem corrigidas: {len(indexs_smaller_file)}")
    print(f"Quantos caminhos exploramos na árvore: {maximum_explore}")
    print(f"Porcentagem de acerto: {correct_matches/len(indexs_smaller_file)}")
    print("#"*64)

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


