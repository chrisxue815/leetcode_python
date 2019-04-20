import unittest
import utils

rotate_to_self = {0, 1, 8}
rotate_to_other = {2, 5, 6, 9}
invalid = {3, 4, 7}


def is_good(num):
    valid = False
    q = num
    while q:
        q, r = divmod(q, 10)
        if r in invalid:
            return False
        if r in rotate_to_other:
            valid = True
    return valid


# O(n) time. O(1) space. Math, hash table.
class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for num in range(1, n + 1):
            if is_good(num):
                count += 1
        return count


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().rotatedDigits(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
