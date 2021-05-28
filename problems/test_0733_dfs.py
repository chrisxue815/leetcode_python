import unittest
from typing import List

import utils

neighbors = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
]

next_neighbor_indexes = [
    [0, 2, 3],
    [1, 2, 3],
    [0, 1, 2],
    [0, 1, 3],
]


# O(n) time. O(n) space. DFS.
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old_color = image[sr][sc]
        if old_color == newColor:
            return image

        rows = len(image)
        cols = len(image[0])

        def dfs(r, c, neighbor_indexes):
            if 0 <= r < rows and 0 <= c < cols and image[r][c] == old_color:
                image[r][c] = newColor
                for i in neighbor_indexes:
                    dr, dc = neighbors[i]
                    dfs(r + dr, c + dc, next_neighbor_indexes[i])

        dfs(sr, sc, [0, 1, 2, 3])
        return image


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
