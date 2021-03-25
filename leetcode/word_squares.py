class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None] * 26
        # isEndOfWord is True if node represent the end of the word
        self.is_end_of_word = False


class Trie:
    # Trie data structure class
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        # Returns new trie node
        return TrieNode()

    def _char_to_index(self, ch):
        # private helper function
        # converts current character into index
        return ord(ch) - ord('a')

    def insert(self, key):
        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        dummy = self.root
        for level in range(len(key)):
            index = self._char_to_index(key[level])
            if not dummy.children[index]:
                dummy.children[index] = self.get_node()
            dummy = dummy.children[index]
        dummy.is_end_of_word = True

    def search(self, key):
        dummy = self.root
        length = len(key)
        for level in range(length):
            index = self._char_to_index(key[level])
            if not dummy.children[index]:
                return False
            dummy = dummy.children[index]
        return dummy



class Solution:
    def wordSquares(self, words):
        trie = Trie()
        for word in words:
            trie.insert(word)


