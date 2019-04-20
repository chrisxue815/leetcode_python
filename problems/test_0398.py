import random
import unittest
from typing import List

import utils


# O(n) space. Reservoir sampling.
class Solution:
    # O(1) time. O(1) space.
    def __init__(self, nums: List[int]):
        self.nums = nums

    # O(n) time. O(1) space.
    def pick(self, target: int) -> int:
        result = -1
        count = 0

        for i, num in enumerate(self.nums):
            if num != target:
                continue

            count += 1
            if random.randrange(count) == 0:
                result = i

        return result


class Test(unittest.TestCase):
    def test(self):
        cls = Solution
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            obj = None

            for func, parameters, expected in zip(case.functions, case.args, case.expected):
                if func == cls.__name__:
                    obj = cls(*parameters)
                else:
                    actual = getattr(obj, func)(*parameters)
                    self.assertIn(actual, expected, msg=args)


if __name__ == '__main__':
    unittest.main()
