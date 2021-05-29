import unittest
from typing import List

import utils


# O(nlog(n)) time. O(n) space. Union-find.
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
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
                if email in owners:
                    root = find_root(owners[email])
                    parents[root] = curr
                else:
                    owners[email] = curr

        for curr, emails in enumerate(accounts):
            root = find_root(curr)
            if root in unions:
                name, union = unions[root]
            else:
                union = set()
                unions[root] = (emails[0], union)
            for email in emails[1:]:
                union.add(email)

        return [[name] + sorted(emails) for name, emails in unions.values()]


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
