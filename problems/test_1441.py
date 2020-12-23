import unittest
from typing import List

import utils


# O(n) time. O(1) space. Iteration, stack.
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        if not target:
            return []

        result = []
        i = 0

        for x in range(1, n + 1):
            result.append('Push')
            if x == target[i]:
                i += 1
                if i >= len(target):
                    break
            else:
                result.append('Pop')

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().buildArray(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
