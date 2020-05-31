import collections
import unittest
from typing import List

import utils
from tree import TreeNode


# O(n) time. O(number of groups) space. Hash table.
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_size_to_groups = collections.defaultdict(list)
        for i, group_size in enumerate(groupSizes):
            groups = group_size_to_groups[group_size]
            if groups and len(groups[-1]) < group_size:
                groups[-1].append(i)
            else:
                groups.append([i])
        return [group for groups in group_size_to_groups.values() for group in groups]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            expected = [tuple(sorted(tuple(sorted(group)) for group in possible_solution))
                        for possible_solution in case.expected]

            actual = Solution().groupThePeople(**case.args.__dict__)

            actual = tuple(sorted(tuple(sorted(group)) for group in actual))
            self.assertIn(actual, expected, msg=args)


if __name__ == '__main__':
    unittest.main()
