import unittest
from typing import List

import utils


# O(V+E) time. O(V) space. Graph, DFS.
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)

        def dfs(cur):
            if visited[cur]:
                return True
            visited[cur] = True

            for nxt in rooms[cur]:
                dfs(nxt)

        dfs(0)

        return all(visited)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
