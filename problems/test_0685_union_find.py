import unittest
import utils


def find_root(parents, node):
    while node != parents[node]:
        node = parents[node]
    return node


# O(nlog(n)) time. O(n) space. Union-find.
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parents = [0] * (len(edges) + 1)
        candidate_a = None
        candidate_b = None
        candidate_b_index = -1

        for index, (parent, child) in enumerate(edges):
            if parents[child] == 0:
                parents[child] = parent
            else:
                candidate_a = [parents[child], child]
                candidate_b = [parent, child]
                candidate_b_index = index
                break

        parents = list(range(len(edges) + 1))

        for index, (parent, child) in enumerate(edges):
            if index == candidate_b_index:
                continue

            root = find_root(parents, parent)

            if root != child:
                parents[child] = parent
            else:
                if candidate_a:
                    return candidate_a
                else:
                    return [parent, child]

        return candidate_b


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().findRedundantDirectedConnection(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
