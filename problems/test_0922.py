import unittest
import utils


# O(n) time. O(1) space. Two pointers.
class Solution(object):
    def sortArrayByParityII(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        even = 0
        odd = 1

        while True:
            while even < len(a) and a[even] & 1 == 0:
                even += 2
            if even >= len(a):
                break

            while odd < len(a) and a[odd] & 1 == 1:
                odd += 2
            if odd >= len(a):
                break

            a[even], a[odd] = a[odd], a[even]
            even += 2
            odd += 2

        return a


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().sortArrayByParityII(**case.args._asdict())
            self.assertItemsEqual(case.args.a, actual)

            for i, num in enumerate(actual):
                self.assertEqual(i & 1, num & 1)


if __name__ == '__main__':
    unittest.main()
