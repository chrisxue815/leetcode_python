import unittest
from typing import List

import utils


class Trie:
    def __init__(self):
        self.val = False
        self.children = {}

    def insert(self, word):
        cur = self
        for c in word:
            c = ord(c) - ord('a')
            if c in cur.children:
                cur = cur.children[c]
            else:
                cur.children[c] = nxt = Trie()
                cur = nxt
        cur.val = True

    def search(self, word, start):
        cur = self
        for i in range(start, len(word)):
            c = ord(word[i]) - ord('a')
            if c not in cur.children:
                return None, i + 1
            cur = cur.children[c]
            if cur.val:
                return cur, i + 1
        return cur if cur.val else None, len(word)


# Backtracking, trie.
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        result = []
        words.sort(key=len)
        root = Trie()

        def dfs(word, start):
            if start >= len(word):
                return True
            cur = root
            while True:
                cur, start = cur.search(word, start)
                if not cur:
                    return False
                if dfs(word, start):
                    return True

        for word in words:
            if not word:
                continue
            if dfs(word, 0):
                result.append(word)
            root.insert(word)

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, asserter=self.assertCountEqual)


if __name__ == '__main__':
    unittest.main()
