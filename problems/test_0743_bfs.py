import heapq
import unittest
import utils


# O(V+E) time. O(V) space. BFS.
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        q = [(0, k)]
        visited = [False] * (n + 1)
        num_visited = 0
        longest_path = 0

        while q:
            path_len, curr = heapq.heappop(q)

            if visited[curr]:
                continue

            visited[curr] = True
            num_visited += 1
            longest_path = path_len

            for next, edge_len in graph[curr]:
                if not visited[next]:
                    heapq.heappush(q, (path_len + edge_len, next))

        return longest_path if num_visited == n else -1


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for i, case in enumerate(cases):
            actual = Solution().networkDelayTime(**case.args._asdict())
            self.assertEqual(case.expected, actual, "i={0}".format(i))


if __name__ == '__main__':
    unittest.main()
