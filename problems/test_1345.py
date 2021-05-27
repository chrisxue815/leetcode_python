import collections
import unittest
from typing import List

import utils


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        d = collections.defaultdict(list)
        for i, num in enumerate(arr):
            d[num].append(i)

        q = collections.deque()
        q.append((0, 0))
        visited, visited_groups = set(), set()

        while q:
            steps, index = q.popleft()
            if index == n - 1:
                return steps

            for neighbor in (index - 1, index + 1):
                if 0 <= neighbor < n and neighbor not in visited:
                    visited.add(neighbor)
                    q.append((steps + 1, neighbor))

            if arr[index] not in visited_groups:
                for neighbor in d[arr[index]]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((steps + 1, neighbor))
                visited_groups.add(arr[index])


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
