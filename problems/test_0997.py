import unittest
import utils


# O(T + N) time. O(N) space. Graph.
class Solution:
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # in-degree - out-degree
        count = [0] * (N + 1)

        for a, b in trust:
            count[a] -= 1
            count[b] += 1

        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i

        return -1


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().findJudge(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
