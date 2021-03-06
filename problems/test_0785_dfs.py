import collections
import unittest
import utils


# O(V+E) time. O(V) space. DFS.
class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        groups = [-1] * len(graph)

        def dfs(a, a_group):
            groups[a] = a_group
            b_group = 1 - a_group

            for b in graph[a]:
                if groups[b] == b_group:
                    continue

                if groups[b] == a_group:
                    return False

                if not dfs(b, b_group):
                    return False
            return True

        for i in range(len(graph)):
            if groups[i] == -1 and not dfs(i, 0):
                return False

        return True


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().isBipartite(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
