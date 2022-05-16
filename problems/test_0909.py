import collections
import unittest
from typing import List

import utils


# O(n) time. O(n) space. BFS.
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        moves = {1: 0}
        q = collections.deque()
        q.append(1)

        while q:
            x = q.popleft()
            for cur in range(x + 1, x + 7):
                a, b = divmod(cur - 1, n)
                nxt = board[n - 1 - a][n - 1 - b if a & 1 else b]
                if nxt > 0:
                    cur = nxt
                if cur == n * n:
                    return moves[x] + 1
                if cur not in moves:
                    moves[cur] = moves[x] + 1
                    q.append(cur)
        return -1


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
