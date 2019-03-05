import heapq
import unittest

import utils


# O(?) time. O(?) space. Heap.
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        curr = 0
        q = [(1, 2)]

        for _ in range(n):
            curr, factor = q[0]

            heapq.heapreplace(q, (curr * 5, 5))
            if factor <= 3:
                heapq.heappush(q, (curr * 3, 3))
                if factor <= 2:
                    heapq.heappush(q, (curr * 2, 2))

        return curr


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().nthUglyNumber(**case.args._asdict())
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
