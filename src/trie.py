from collections import UserDict

class WordNode(UserDict):
    """
    Used to mark a node as a word in the Trie structure.
    """
    pass
    

class Trie:
    
    def __init__(self):
        self.root = {}
        self.n_words = 0
            
    def insert(self, word: str):
        """Insert a word in the trie structure with
        a marker for the last character which is used to identify 
        a word in the structure. 
        
        Args:
            word: word to insert.

        Returns:
            True when the word is correctly inserted.
            False when the word already exists in the structure.
        """
        
        if self.find(word):
            return False
        

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
        self.n_words += 1
        if value is None:
            node.setdefault(last_char, WordNode())
        else:
            node[last_char] = WordNode(node[last_char])
            
        return True
                
    def find(self, word: str):
        """Retrieve a word in the structure if exists.
        
        Args:
            word: word to retrieve.

        Returns:
            True when the word is found.
            False when the word does not exists.
        """   
        
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
                
        if isinstance(node ,WordNode): 
            return True 
        else: 
            return False
        
    def __str__(self):
        return str(self.root)
    
    def infer_possible_paths(self):
        pass
       
