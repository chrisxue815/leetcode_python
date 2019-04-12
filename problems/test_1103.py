import unittest
from typing import List

import math

import utils


# O(n) time. O(1) space. Algebra, arithmetic progression.
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        repeat = int((math.sqrt(1 + 8 * candies) - 1) / 2)
        num_rounds, extra_people = divmod(repeat, num_people)

        for i in range(num_people):
            num_rounds_for_me = num_rounds + (i < extra_people)
            a1 = i + 1
            an = a1 + num_people * (num_rounds_for_me - 1)
            result[i] = (a1 + an) * num_rounds_for_me // 2

        extra_candies = candies - (1 + repeat) * repeat // 2
        if extra_candies:
            person_got_extra_candies = repeat % num_people
            result[person_got_extra_candies] += extra_candies

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().distributeCandies(**case.args._asdict())
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
