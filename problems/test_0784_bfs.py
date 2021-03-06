import unittest
import utils


# O(2^n) time. O(1) space. BFS.
class Solution:
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

            for j in range(len(result)):
                clone = list(result[j])
                clone[i] = new_ch
                result.append(clone)

        for i, s in enumerate(result):
            result[i] = ''.join(s)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().letterCasePermutation(**case.args.__dict__)
            self.assertCountEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
