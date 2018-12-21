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
        person_to_admirers = [[] for _ in xrange(N + 1)]

        for a, b in trust:
            person_to_admirers[b].append(a)

        judge = 0

        for person, admirers in enumerate(person_to_admirers):
            if len(admirers) == N - 1:
                if judge == 0:
                    judge = person
                else:
                    return -1

        return judge if judge != 0 and all(a != judge for a, b in trust) else -1


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p997.json').test_cases

        for case in cases:
            actual = Solution().findJudge(case.N, case.trust)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
