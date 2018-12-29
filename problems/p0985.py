import unittest
import utils


# O(n) time. O(1) space. Algebra.
class Solution(object):
    def sumEvenAfterQueries(self, a, queries):
        """
        :type a: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = []
        answer = sum(val for val in a if val & 1 == 0)

        for val, index in queries:
            if a[index] & 1 == 0:
                answer -= a[index]

            a[index] += val

            if a[index] & 1 == 0:
                answer += a[index]

            result.append(answer)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().sumEvenAfterQueries(case.a, case.queries)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
