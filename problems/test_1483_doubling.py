import unittest
from typing import List

import utils


# Doubling, bit manipulation.
class TreeAncestor:

    # O(nlog(n)) time. O(nlog(n)) space.
    def __init__(self, n: int, parent: List[int]):
        self.parents = parents = [[-1] * n if i > 0 else parent for i in range(16)]

        for i in range(1, len(parents)):
            prev = parents[i - 1]
            curr = parents[i]
            for node in range(n):
                p = prev[node]
                if p != -1:
                    curr[node] = prev[p]

    # O(log(k)) time. O(1) space.
    def getKthAncestor(self, node: int, k: int) -> int:
        for parent in self.parents:
            if k == 0:
                break
            if k & 1:
                node = parent[node]
                if node == -1:
                    break
            k >>= 1
        return node


class Test(unittest.TestCase):
    def test(self):
        utils.test_invocations(self, __file__, TreeAncestor)


if __name__ == '__main__':
    unittest.main()
