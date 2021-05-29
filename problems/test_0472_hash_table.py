import unittest
from typing import List

import utils


# Backtracking, hash table.
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        result = []
        words.sort(key=len)
        visited = set()
        min_length = max(1, len(words[0]))

        def dfs(word):
            if word in visited:
                return True
            return any(word[:end] in visited and dfs(word[end:])
                       for end in range(min_length, len(word) - min_length + 1))

        for word in words:
            if dfs(word):
                result.append(word)
            visited.add(word)

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, asserter=self.assertCountEqual)


if __name__ == '__main__':
    unittest.main()
