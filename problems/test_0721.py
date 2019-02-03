import unittest
import utils


def find_root(parents, node):
    root = node
    while root != parents[root]:
        root = parents[root]
    while node != root:
        node, parents[node] = parents[node], root
    return root


# O(nlog(n)) time. O(n) space. Union-find.
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        parents = list(range(len(accounts)))
        email_to_id = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                j = email_to_id.get(email, -1)
                if j == -1:
                    email_to_id[email] = i
                else:
                    root = find_root(parents, j)
                    parents[root] = i

        id_to_account = {}

        for i, account in enumerate(accounts):
            root = find_root(parents, i)
            merged = id_to_account.get(root, None)
            if not merged:
                id_to_account[root] = merged = (account[0], set())
            for email in account[1:]:
                merged[1].add(email)

        return [[name] + list(sorted(emails)) for name, emails in id_to_account.values()]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().accountsMerge(**vars(case.args))
            self.assertItemsEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
