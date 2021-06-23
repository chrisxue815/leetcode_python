import unittest
from typing import List

import utils


class Trie(dict):
    def __init__(self, val):
        super().__init__()
        self.val = val

    def __missing__(self, key):
        curr = Trie(self.val)
        self[key] = curr
        return curr

    def add(self, s):
        curr = self
        for ch in s:
            curr = curr[ch]
        return curr


# O(len(s)! / (min_len(wordDict) - 1)!) time. O(total_len(wordDict)) space. Trie, backtracking. TLE.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie(False)

        for word in wordDict:
            trie.add(word).val = True

        def dfs(start):
            if start == len(s):
                return True

            curr = trie
            for i in range(start, len(s)):
                curr = curr.get(s[i])
                if curr is None:
                    break
                if curr.val and dfs(i + 1):
                    return True

            return False

        return dfs(0)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
