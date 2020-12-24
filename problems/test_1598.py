import unittest
from typing import List

import utils


# O(n) time. O(1) space. Iteration.
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = 0

        for log in logs:
            if log.startswith('.'):
                if len(log) == 3 and result > 0:
                    result -= 1
            else:
                result += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().minOperations(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
