import unittest
from typing import List

import utils


# O(n) time. O(1) space.
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        forward = sum(distance[start:destination])
        backward = sum(distance[:start]) + sum(distance[destination:])

        return min(forward, backward)


class Test(unittest.TestCase):
    def test(self):
        func_name = next(f for f in dir(Solution) if not f.startswith('__'))
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            func = getattr(Solution(), func_name)
            actual = func(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
