import heapq
import unittest

import utils


# O(nlog(n)) time. O(n) space. Heap.
class Solution:
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        q = [-stone for stone in stones]
        heapq.heapify(q)

        while len(q) > 1:
            y = heapq.heappop(q)
            x = q[0]
            heapq.heapreplace(q, y - x)

        return -q[0]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().lastStoneWeight(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
