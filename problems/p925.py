import unittest
import utils


# O(n) time. O(1) space. Two pointers.
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if not name:
            return not typed
        if not typed:
            return False
        if name[0] != typed[0]:
            return False

        j = 1

        for i in xrange(1, len(name)):
            if name[i] != name[i - 1]:
                while j < len(typed) and typed[j] == name[i - 1]:
                    j += 1

            if j >= len(typed):
                return False

            if name[i] != typed[j]:
                return False

            j += 1

        while j < len(typed) and typed[j] == name[-1]:
            j += 1

        return j == len(typed)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p925.json').test_cases

        for case in cases:
            actual = Solution().isLongPressedName(case.name, case.typed)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
