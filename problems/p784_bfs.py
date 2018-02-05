import unittest
import utils


# O(2^n) time. O(1) space. BFS.
class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s = list(s)
        result = [s]

        for i, ch in enumerate(s):
            if ch.isdigit():
                continue

            new_ch = ch.lower() if ch.isupper() else ch.upper()

            for j in xrange(len(result)):
                clone = list(result[j])
                clone[i] = new_ch
                result.append(clone)

        for i, s in enumerate(result):
            result[i] = ''.join(s)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p784.json').test_cases

        for case in cases:
            actual = Solution().letterCasePermutation(case.s)
            self.assertItemsEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
