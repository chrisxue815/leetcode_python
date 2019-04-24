import unittest
from typing import List

import utils


# O(n) time. O(1) space. Floyd's tortoise and hare cycle detection algorithm.
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        for start, move in enumerate(nums):
            if move == 0:
                continue

            t = h = start
            forward = move > 0

            def advance(curr):
                move = nums[curr]
                if move == 0 or (move > 0) != forward:
                    return False, curr
                nxt = (curr + move) % n
                return nxt != curr, nxt

            while True:
                ok, h = advance(h)
                if not ok:
                    break

                ok, h = advance(h)
                if not ok:
                    break

                ok, t = advance(t)

                if t == h:
                    return True

            t = start

            while True:
                ok, nxt = advance(t)
                if not ok:
                    break

                nums[t] = 0
                t = nxt

        return False


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().circularArrayLoop(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
