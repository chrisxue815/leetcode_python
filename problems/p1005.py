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

        for i, num in enumerate(A):
            if i >= K or num >= 0:
                break
            A[i] = -num
        else:
            i = len(A)

        K -= i

        if K & 1:
            min_index = i - 1 if i == len(A) or A[i - 1] < A[i] else i
            A[min_index] = -A[min_index]

        return sum(A)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().largestSumAfterKNegations(**vars(case.args))
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
