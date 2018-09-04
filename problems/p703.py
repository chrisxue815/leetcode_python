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
        cases = utils.load_json_from_path('../leetcode_test_cases/p703.json').test_cases

        for case in cases:
            obj = KthLargest(case.k, case.nums)

            for query in case.queries:
                actual = obj.add(query.val)
                self.assertEqual(query.expected, actual)


if __name__ == '__main__':
    unittest.main()
