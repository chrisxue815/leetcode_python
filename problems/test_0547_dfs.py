import unittest
from typing import List

import utils


# O(n) time. O(n) space. DFS.
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            if isConnected[i][i] == 0:
                return False
            isConnected[i][i] = 0
            for j in range(i):
                if isConnected[j][i]:
                    dfs(j)
            for j in range(i + 1, len(isConnected)):
                if isConnected[i][j]:
                    dfs(j)
            return True

        result = 0
        for i in range(len(isConnected)):
            if dfs(i):
                result += 1
        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
