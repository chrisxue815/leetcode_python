import unittest
from typing import List

import utils


# O(n) time. O(n) space. Hash table.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i, num in enumerate(nums):
            j = visited.get(target - num, -1)
            if j != -1:
                return [j, i]

            visited[num] = i


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
