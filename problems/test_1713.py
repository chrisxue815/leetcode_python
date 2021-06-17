import bisect
import unittest
from typing import List

import utils


# O(nlog(n)) time. O(n) space. Greedy, binary search.
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        indexes = {a: i for i, a in enumerate(target)}
        stack = []
        for a in arr:
            if a not in indexes:
                continue
            index = indexes[a]
            i = bisect.bisect_left(stack, index)
            if i < len(stack):
                stack[i] = index
            else:
                stack.append(index)
        return len(target) - len(stack)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
