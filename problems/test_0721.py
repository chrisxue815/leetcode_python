import unittest

import utils


# O(nlog(n)) time. O(n) space. Union-find.
class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        parents = list(range(len(accounts)))
        owners = {}
        unions = {}

        def find_root(node):
            root = node
            while root != parents[root]:
                root = parents[root]
            while node != root:
                node, parents[node] = parents[node], root
            return root

        for curr, emails in enumerate(accounts):
            for email in emails[1:]:
                prev = owners.get(email, -1)
                if prev == -1:
                    owners[email] = curr
                else:
                    root = find_root(prev)
                    parents[root] = curr

        for curr, emails in enumerate(accounts):
            root = find_root(curr)
            union = unions.get(root)
            if not union:
                unions[root] = union = (emails[0], set())
            for email in emails[1:]:
                union[1].add(email)

        return [[name] + list(sorted(emails)) for name, emails in unions.values()]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().accountsMerge(**case.args.__dict__)
            self.assertCountEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
