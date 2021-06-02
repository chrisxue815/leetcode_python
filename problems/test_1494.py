import itertools
import unittest
from typing import List

import utils


# Backtracking, bitmask, memorization, graph
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        prevs = [[] for _ in range(n + 1)]
        has_next = [False] * (n + 1)
        cache = {(1 << n) - 1: 0}
        for a, b in relations:
            prevs[b].append(a)
            has_next[a] = True

        def dfs(bitmask):
            if bitmask in cache:
                return cache[bitmask]

            pending = []
            for i in range(1, n + 1):
                if bitmask & (1 << (i - 1)):
                    continue
                if all(bitmask & (1 << (j - 1)) for j in prevs[i]):
                    pending.append(i)

            if len(pending) <= k:
                cache[bitmask] = 1 + dfs(bitmask + sum(1 << (i - 1) for i in pending))
                return cache[bitmask]

            with_next = []
            without_next = []
            for i in pending:
                if has_next[i]:
                    with_next.append(i)
                else:
                    without_next.append(i)

            if len(with_next) <= k:
                with_next += without_next[:k - len(with_next)]
                cache[bitmask] = 1 + dfs(bitmask + sum(1 << (i - 1) for i in with_next))
            else:
                cache[bitmask] = 1 + min(dfs(bitmask + sum(1 << (i - 1) for i in combination))
                                         for combination in itertools.combinations(with_next, k))
            return cache[bitmask]

        return dfs(0)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
