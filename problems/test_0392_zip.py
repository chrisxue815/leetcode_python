import unittest

import utils


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        s_index = 0
        s_val = s[s_index]
        for t_val in t:
            if t_val == s_val:
                s_index += 1
                if s_index == len(s):
                    return True
                s_val = s[s_index]
        return False


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
