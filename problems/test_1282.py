import collections
import unittest
from typing import List

import utils
from tree import TreeNode


# O(n) time. O(number of groups) space. Hash table.
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_size_to_people = collections.defaultdict(list)

        for person, group_size in enumerate(groupSizes):
            group_size_to_people[group_size].append(person)

        return [people[i:i + group_size] for group_size, people in
                group_size_to_people.items() for i in range(0, len(people), group_size)]


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
