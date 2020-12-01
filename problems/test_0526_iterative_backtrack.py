import unittest

import utils


def permutations(n):
    nums = list(range(1, n + 1))
    cycles = list(range(n))
    yield tuple(nums)

    while True:
        for i in range(n - 1, -1, -1):
            cycles[i] += 1
            j = cycles[i]

            if j < n:
                nums[i], nums[j] = nums[j], nums[i]
                yield tuple(nums)
                break
            else:
                cycles[i] = i
                nums[i:] = nums[i + 1:] + [nums[i]]
        else:
            return


def is_beautiful(index, num):
    if index == num:
        return True
    elif index > num:
        return index % num == 0
    else:
        return num % index == 0


# O(n!) time. O(n) space. Backtracking, iterative permutation.
class Solution:
    def countArrangement(self, N: int) -> int:
        count = 0
        for permutation in permutations(N):
            for index, num in enumerate(permutation):
                if not is_beautiful(index + 1, num):
                    break
            else:
                count += 1
        return count


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().countArrangement(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
