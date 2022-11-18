def test_load_data_trie(full_trie_with_execution_time):
    full_trie, execution_time = full_trie_with_execution_time 
    assert full_trie.n_words == 370105
    assert  execution_time <= 4.0