import heapq
import unittest

import utils


# O(log(k)) time. O(k) space. Binary heap.
class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        k_largest = []

        for num in nums[:k]:
            heapq.heappush(k_largest, num)

        for num in nums[k:]:
            heapq.heappushpop(k_largest, num)

        self.k_largest = k_largest
        self.k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.k_largest) < self.k:
            heapq.heappush(self.k_largest, val)
        else:
            heapq.heappushpop(self.k_largest, val)

        return self.k_largest[0]


class Test(unittest.TestCase):
    def test(self):
        cls = KthLargest
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            obj = None

            for func, parameters, expected in zip(case.functions, case.args, case.expected):
                if func == cls.__name__:
                    obj = cls(*parameters)
                else:
                    actual = getattr(obj, func)(*parameters)
                    self.assertEqual(expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
