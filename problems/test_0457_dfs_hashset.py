import unittest
from typing import List

import utils


# O(n) time. O(n) space. DFS, hash set.
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        for start, move in enumerate(nums):
            if move == 0:
                continue

            forward = move > 0
            curr = start
            visited = set()
            visited.add(curr)

            while True:
                move = nums[curr]
                if move == 0 or (move > 0) != forward:
                    break
                nums[curr] = 0

                nxt = (curr + move) % n
                if nxt == curr:
                    break

                if nxt in visited:
                    return True
                visited.add(nxt)

                curr = nxt

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
