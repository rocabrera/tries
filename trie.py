from collections import UserDict

class WordNode(UserDict):
    """
    Usado para indicar que finaliza uma palavra contida no dicionário (dataset). 
    """
    pass
    

class Trie:
    
    def __init__(self):
        self.root = {}
        
    def insert(self, word: str):
        
        node = self.root
        for char in word[:-1]:
            value = node.get(char)   
            if value is None:
                next_node = {}
                node.setdefault(char, next_node)
                node = next_node
            else:
                node = value
                
        # Logic to identify node as a word
        last_char = word[-1]
        value = node.get(last_char)   
        
        if value is None:
            node.setdefault(last_char, WordNode())
        else:
            node[last_char] = WordNode(node[last_char])
                
    def find(self, word: str):
        
        node = self.root
        
        matches = []
        
        for char in word:
            
            value = node.get(char)
            
            if value is None:
                # self.infer_possible_paths()
                return False
            
            else:
                matches.append(char)
                node = value
                
        if isinstance(node ,WordNode): return True 
        else: return False
        
    def __str__(self):
        return str(self.root)
    
    def infer_possible_paths(self):
        pass
        