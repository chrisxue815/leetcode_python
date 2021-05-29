import collections
import unittest
from typing import List

import utils

target = (1, 2, 3, 4, 5, 0)

swaps = [
    [1, 3],
    [0, 2, 4],
    [1, 5],
    [0, 4],
    [1, 3, 5],
    [2, 4],
]


# BFS, shortest path.
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        cur = tuple(cell for row in board for cell in row)
        zero_index = cur.index(0)
        q = collections.deque()
        q.append((0, zero_index, cur))
        visited = set()

        while q:
            distance, zero_index, cur = q.popleft()
            if cur in visited:
                continue
            if cur == target:
                return distance
            visited.add(cur)

            for swap in swaps[zero_index]:
                nxt = list(cur)
                nxt[zero_index], nxt[swap] = nxt[swap], nxt[zero_index]
                nxt = tuple(nxt)
                if nxt not in visited:
                    q.append((distance + 1, swap, nxt))

        return -1


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
