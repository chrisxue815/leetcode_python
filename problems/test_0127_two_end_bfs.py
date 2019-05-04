import collections
import unittest
from typing import List

import utils


# O(n) time. O(n) space. Two-end BFS.
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        graph = collections.defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                wildcard = word[:i] + '.' + word[i + 1:]
                graph[wildcard].add(word)

        result = 2
        visited = {beginWord, endWord}
        begin = {beginWord}
        end = {endWord}

        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin

            next_set = set()

            for word in begin:
                for i in range(len(word)):
                    wildcard = word[:i] + '.' + word[i + 1:]
                    for nxt in graph[wildcard]:
                        if nxt in end:
                            return result
                        if nxt not in visited:
                            visited.add(nxt)
                            next_set.add(nxt)

            begin = next_set
            result += 1

        return 0


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().ladderLength(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
