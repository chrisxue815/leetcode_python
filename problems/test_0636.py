import unittest
from typing import List

import utils


# O(n) time. O(depth) space. Stack.
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            func, action, time = log.split(':')
            func = int(func)
            time = int(time)

            if action.startswith('s'):
                if stack:
                    result[stack[-1]] += time - prev_time
                stack.append(func)
            else:
                time += 1
                result[func] += time - prev_time
                stack.pop()

            prev_time = time

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().exclusiveTime(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
