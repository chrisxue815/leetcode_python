import unittest

import utils


class Solution:
    def numTrees(self, n: int) -> int:
        f = [1, 1]
        for i in range(2, n + 1):
            fi = 0
            for j in range(1, i + 1):
                fi += f[j - 1] * f[i - j]
            f.append(fi)

        return f[n]


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
