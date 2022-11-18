import pytest

from trie import Trie

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

