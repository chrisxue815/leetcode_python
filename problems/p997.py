import unittest
import utils


# O(T + N) time. O(N) space. Graph.
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        outgoing = [0] * (N + 1)
        incoming = [0] * (N + 1)

        for a, b in trust:
            outgoing[a] += 1
            incoming[b] += 1

        judge = 0

        for person, num_admirers in enumerate(incoming):
            if num_admirers == N - 1 and outgoing[person] == 0:
                if judge == 0:
                    judge = person
                else:
                    return -1

        return judge if judge != 0 else -1


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p997.json').test_cases

        for case in cases:
            actual = Solution().findJudge(case.N, case.trust)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
