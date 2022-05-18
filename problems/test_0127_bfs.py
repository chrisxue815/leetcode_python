import collections
import unittest
from typing import List

import utils


# O(n) time. O(n) space. BFS.
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
        q = collections.deque()
        q.append((1, beginWord))

        while q:
            distance, curr = q.pop()
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
                        q.append((distance, nxt))

        return 0


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
