import unittest
from typing import List

import utils


# O(n) time. O(1) space. Greedy.
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bills_5 = bills_10 = bills_20 = 0

        for bill in bills:
            if bill == 5:
                bills_5 += 1
            elif bill == 10:
                if bills_5 >= 1:
                    bills_5 -= 1
                    bills_10 += 1
                else:
                    return False
            else:
                if bills_5 >= 1 and bills_10 >= 1:
                    bills_5 -= 1
                    bills_10 -= 1
                    bills_20 += 1
                elif bills_5 >= 3:
                    bills_5 -= 3
                    bills_20 += 1
                else:
                    return False

        return True


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
