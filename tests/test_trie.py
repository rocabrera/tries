def test_trie_find_suffix(trie_with_suffix):
    
    assert trie_with_suffix.find("testtes")
    assert trie_with_suffix.find("test")
    assert trie_with_suffix.find("testte")
    assert not trie_with_suffix.find("tes")
    

def test_trie_find_prefix(trie_with_prefix):
    
    assert trie_with_prefix.find("amor")
    assert trie_with_prefix.find("aamor")
    assert trie_with_prefix.find("aammor")
    assert not trie_with_prefix.find("a")
    