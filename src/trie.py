from collections import UserDict
from src.levenshtein import lev_dist
from typing import Tuple, Union

class WordNode(UserDict):
    """
    Used to mark a node as a word in the Trie structure.
    """
    def set_word(self, word:str):
        self.word = word

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
        result, _ = self.find(word)
        if result:
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
            word_node = WordNode()
            word_node.set_word(word)
            node.setdefault(last_char, word_node)
        else:
            word_node = WordNode(node[last_char])
            word_node.set_word(word)
            node[last_char] = word_node

        return True

    def find(self, word: str, correction: bool = False, threshold: int=3, maximum_explore:int = None) -> Tuple[bool, Union[str,None]]:
        """Retrieve a word in the structure if exists.

        Args:
            word: word to retrieve.

        Returns:
            True when the word is found.
            False when the word does not exists.
        """

        node = self.root


        for char in word:

            next_node = node.get(char)

            # If the character does not exist in the node the word does not exist.
            if next_node is None:
                if correction:
                    possible_matches = self._correct(node, maximum_explore)
                    score, best_word = min(
                            ((lev_dist(word, possible_word),
                              possible_word) for possible_word in possible_matches),
                            key=lambda x:x[0])
                    if score <= threshold:
                        return (True, best_word)
                    else:
                        return (False, word)


                return (False, None)

            else:
                node = next_node

        if isinstance(node ,WordNode):
            return (True, node.word)
        else:
            return (False, None)

    def find_with_correction(self, word:str, maximum_explore:int = None):

        result, word = self.find(word, correction=True, maximum_explore=maximum_explore)

        if word is not None:
            return word
        else:
            return "NOT_FIXABLE"


    def __str__(self):
        return str(self.root)

    def _correct(self, root_node:dict, maximum_explore:int = None):

        possible_matches = []

        explore_nodes = [root_node]

        while len(explore_nodes) != 0:

            node = explore_nodes.pop()

            if isinstance(node, WordNode):
                possible_matches.append(node.word)

            if node is not None:

                next_chars = list(node.keys())
                next_nodes = [node.get(char) for char in next_chars]
                explore_nodes.extend(next_nodes)

            if maximum_explore is not None:
                if len(possible_matches) >= maximum_explore:
                    return possible_matches
            
        return possible_matches