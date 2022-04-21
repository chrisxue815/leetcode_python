import unittest
from typing import List

import utils


# Queue.
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while sandwiches:
            for _ in range(len(students)):
                if students[0] == sandwiches[0]:
                    students.pop(0)
                    sandwiches.pop(0)
                    break
                else:
                    front = students.pop(0)
                    students.append(front)
            else:
                return len(students)

        return 0


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
