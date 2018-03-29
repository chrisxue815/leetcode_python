from undirected_graph import *
import unittest
import utils


# O(V+E) time. O(V) space. DFS.
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None

        nodes = {}

        def clone(a):
            b = nodes.get(a.label, None)
            if b:
                return b

            b = UndirectedGraphNode(a.label)
            nodes[b.label] = b
            b.neighbors = [clone(neighbor) for neighbor in a.neighbors]
            return b

        return clone(node)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p133.json').test_cases

        for case in cases:
            nodes = UndirectedGraphNode.parse(case.graph)
            for node in nodes.itervalues():
                actual = Solution().cloneGraph(node)
                self.assertEqual(node, actual)


if __name__ == '__main__':
    unittest.main()
