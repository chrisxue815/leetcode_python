import collections
import unittest
from typing import List

import utils


# O(n) time. O(1) space. Math, hash table.
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = list(collections.Counter(tasks).values())
        max_count = max(counts)
        max_count_freq = counts.count(max_count)
        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_freq)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
