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
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    # O(n) time. O(n) space.
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.root.search(word, True).value = True

    # O(n) time. O(1) space.
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        leaf = self.root.search(word, False)
        return leaf is not None and leaf.value

    # O(n) time. O(1) space.
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.root.search(prefix, False) is not None


class Test(unittest.TestCase):
    def test(self):
        cls = Trie
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            obj = None

            for func, parameters, expected in zip(case.functions, case.args, case.expected):
                if func == cls.__name__:
                    obj = cls(*parameters)
                else:
                    actual = getattr(obj, func)(*parameters)
                    self.assertEqual(expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
