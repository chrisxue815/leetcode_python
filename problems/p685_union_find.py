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

        parents = range(len(edges) + 1)

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
        cases = utils.load_json_from_path('../leetcode_test_cases/p684.json').test_cases

        for case in cases:
            actual = Solution().findRedundantDirectedConnection(case.edges)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()