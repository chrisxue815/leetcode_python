import unittest
from typing import List

import utils


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


# O(n) time. O(n) space. Hash table, Recursive DFS.
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees = {employee.id: employee for employee in employees}

        def dfs(manager):
            subordinate_sum = sum(dfs(employees[subordinate]) for subordinate in manager.subordinates)
            return manager.importance + subordinate_sum

        return dfs(employees[id])


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=self.process_args)

    def process_args(self, args):
        args.employees = [Employee(*employee) for employee in args.employees]


if __name__ == '__main__':
    unittest.main()
