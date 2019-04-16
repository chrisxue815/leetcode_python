import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def toGoatLatin(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''

        for i, word in enumerate(s.split()):
            if word[0].lower() in 'aeiou':
                result += word + 'ma' + 'a' * (i + 1) + ' '
            else:
                result += word[1:] + word[0] + 'ma' + 'a' * (i + 1) + ' '

        return result[:-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().toGoatLatin(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
