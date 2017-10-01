import unittest


# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


# O(n). Hash table, DFS.
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        employees = {employee.id: employee for employee in employees}

        def calc_importance(manager):
            subordinate_sum = sum(calc_importance(employees[subordinate]) for subordinate in manager.subordinates)
            return manager.importance + subordinate_sum

        return calc_importance(employees[id])


class Test(unittest.TestCase):
    def test(self):
        self._test([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1, 11)

    def _test(self, employees, id, expected):
        employees = [Employee(*employee) for employee in employees]
        actual = Solution().getImportance(employees, id)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
