import unittest
import utils


# O(V+E) time. O(V) space. DFS.
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        visited = [False] * len(graph)
        path = [0]
        paths = []

        def dfs(i):
            if i == len(graph) - 1:
                paths.append(list(path))
                return

            for j in graph[i]:
                if visited[j]:
                    continue

                visited[j] = True
                path.append(j)

                dfs(j)

                path.pop()
                visited[j] = False

        dfs(0)
        return paths


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().allPathsSourceTarget(**case.args._asdict())
            self.assertCountEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
