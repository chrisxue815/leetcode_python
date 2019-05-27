import unittest


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


class Solution:
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for permutation in permutations(n):
            for index, num in enumerate(permutation):
                if not is_beautiful(index + 1, num):
                    break
            else:
                count += 1
        return count


class Test(unittest.TestCase):
    def test(self):
        self._test(1, 1)
        self._test(2, 2)
        self._test(3, 3)
        self._test(7, 41)

    def _test(self, n, expected):
        actual = Solution().countArrangement(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
