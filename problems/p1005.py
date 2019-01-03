import collections
import unittest
import utils


# O(nlog(n)) time. O(n) space. Algebra, sorting.
class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()

        num_negative = 0
        for num in A:
            if num < 0:
                num_negative += 1
            else:
                break

        for i in xrange(min(K, num_negative)):
            A[i] = -A[i]

        K -= num_negative
        if K > 0 and K & 1:
            smaller_index = num_negative - 1 if A[num_negative - 1] < A[num_negative] else num_negative
            A[smaller_index] = -A[smaller_index]

        return sum(A)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().largestSumAfterKNegations(case.A, case.K)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
