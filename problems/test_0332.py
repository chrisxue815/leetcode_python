import collections
import heapq
import unittest
import utils


# O(V+E) time. O(V) space. Hierholzer, DFS.
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = collections.defaultdict(list)

        for origin, dest in tickets:
            heapq.heappush(graph[origin], dest)

        route = []

        def dfs(node):
            successors = graph[node]
            while successors:
                dfs(heapq.heappop(successors))
            route.append(node)

        dfs('JFK')
        return route[::-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().findItinerary(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
