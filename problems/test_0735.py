import unittest
from typing import List

import utils


# O(n) time. O(1) space. Stack.
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack:
                    if stack[-1] < 0:
                        stack.append(asteroid)
                        break
                    if stack[-1] > -asteroid:
                        break
                    elif stack[-1] == -asteroid:
                        stack.pop()
                        break
                    else:
                        stack.pop()
                else:
                    stack.append(asteroid)

        return stack


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().asteroidCollision(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
