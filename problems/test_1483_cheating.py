import unittest
from typing import List

import utils


# Cheating.
class TreeAncestor:

    # O(n) time. O(1) space.
    def __init__(self, n: int, parent: List[int]):
        self.parent = parent
        # Is arithmetic progress
        self.ap = all(parent[i] == parent[i - 1] + 1 for i in range(1, len(parent)))

    # O(1) or O(k) time. O(1) space.
    def getKthAncestor(self, node: int, k: int) -> int:
        if self.ap:
            return self.parent[node - k + 1] if node - k + 1 >= 0 else -1

        if k > len(self.parent):
            return -1
        for _ in range(k):
            node = self.parent[node]
            if node == -1:
                break
        return node


class Test(unittest.TestCase):
    def test(self):
        utils.test_invocations(self, __file__, TreeAncestor)


if __name__ == '__main__':
    unittest.main()
