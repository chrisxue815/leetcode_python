import unittest

import utils
from undirected_graph import *


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
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            nodes = UndirectedGraphNode.parse(case.args.graph)
            for node in nodes.values():
                actual = Solution().cloneGraph(node)
                self.assertEqual(node, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
