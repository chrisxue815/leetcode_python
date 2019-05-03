import collections
import heapq
import unittest
from typing import List

import utils


# O(n) time. O(n) space. Graph.
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        graph = collections.defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                wildcard = word[:i] + '.' + word[i + 1:]
                graph[wildcard].add(word)

        visited = set()
        q = [(1, beginWord)]

        while q:
            distance, curr = heapq.heappop(q)
            if curr in visited:
                continue
            visited.add(curr)

            distance += 1

            for i in range(len(curr)):
                nxt_wildcard = curr[:i] + '.' + curr[i + 1:]
                for nxt in graph[nxt_wildcard]:
                    if nxt == endWord:
                        return distance
                    if nxt not in visited:
                        heapq.heappush(q, (distance, nxt))

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
