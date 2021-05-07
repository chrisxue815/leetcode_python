import unittest
from typing import List

import utils


# O(n) time. O(1) space. Math, array.
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        max_count = 0
        max_count_freq = 0

        for task in tasks:
            index = ord(task) - ord('A')
            counts[index] += 1
            if max_count == counts[index]:
                max_count_freq += 1
            elif max_count < counts[index]:
                max_count = counts[index]
                max_count_freq = 1

        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_freq)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
