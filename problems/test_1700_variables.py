import unittest
from typing import List

import utils


# O(n) time. O(1) space.
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ones = sum(students)
        zeros = len(students) - ones

        for i, sandwich in enumerate(sandwiches):
            if sandwich:
                if ones <= 0:
                    return len(sandwiches) - i
                ones -= 1
            else:
                if zeros <= 0:
                    return len(sandwiches) - i
                zeros -= 1

        return 0


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
