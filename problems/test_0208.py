import unittest

import utils


class TrieNode:
    def __init__(self):
        self.value = False
        self.children = [None] * 26

    def get(self, ch, add):
        index = ord(ch) - ord('a')
        child = self.children[index]

        if not child and add:
            child = TrieNode()
            self.children[index] = child

        return child

    def search(self, word, add):
        curr = self

        for ch in word:
            curr = curr.get(ch, add)
            if not curr:
                return curr

        return curr


# O(total length of words) space.
class Trie:
    # O(1) time. O(1) space.
    def __init__(self):
        self.root = TrieNode()

    # O(n) time. O(n) space.
    def insert(self, word: str) -> None:
        self.root.search(word, True).value = True

    # O(n) time. O(1) space.
    def search(self, word: str) -> bool:
        leaf = self.root.search(word, False)
        return leaf is not None and leaf.value

    # O(n) time. O(1) space.
    def startsWith(self, prefix: str) -> bool:
        return self.root.search(prefix, False) is not None


class Test(unittest.TestCase):
    def test(self):
        utils.test_invocations(self, __file__, Trie)


if __name__ == '__main__':
    unittest.main()
