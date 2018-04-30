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
        cases = utils.load_json_from_path('../leetcode_test_cases/p797.json').test_cases

        for case in cases:
            actual = Solution().allPathsSourceTarget(case.graph)
            self.assertItemsEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
