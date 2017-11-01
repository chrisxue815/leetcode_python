import unittest


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """

        def _dfs(path, lo, val, multi):
            if lo == len(num):
                if val == target:
                    result.append(''.join(path))
                return

            max_hi = lo + 2 if num[lo] == '0' else len(num) + 1

            for hi in xrange(lo + 1, max_hi):
                curr_str = num[lo:hi]
                curr_int = int(curr_str)
                if lo == 0:
                    _dfs(curr_str, hi, curr_int, curr_int)
                else:
                    _dfs(path + '+' + curr_str, hi, val + curr_int, curr_int)
                    _dfs(path + '-' + curr_str, hi, val - curr_int, -curr_int)
                    _dfs(path + '*' + curr_str, hi, val - multi + multi * curr_int, multi * curr_int)

        result = []
        _dfs('', 0, 0, 0)
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test("123", 6, ["1+2+3", "1*2*3"])
        self._test("232", 8, ["2*3+2", "2+3*2"])
        self._test("105", 5, ["1*0+5", "10-5"])
        self._test("00", 0, ["0+0", "0-0", "0*0"])
        self._test("3456237490", 9191, [])

    def _test(self, num, target, expected):
        actual = Solution().addOperators(num, target)
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
