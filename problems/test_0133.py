import unittest

import utils
from undirected_graph import *


# O(V+E) time. O(V) space. DFS.
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        nodes = {}

        def clone(a):
            b = nodes.get(a.val, None)
            if b:
                return b

            b = Node(a.val)
            nodes[b.val] = b
            b.neighbors = [clone(neighbor) for neighbor in a.neighbors]
            return b

        return clone(node)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            nodes = Node.parse(case.args.graph)
            for node in nodes.values():
                actual = Solution().cloneGraph(node)
                self.assertEqual(node, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
