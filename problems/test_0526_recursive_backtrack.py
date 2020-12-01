import unittest

import utils


def permutations(n):
    result = []
    _permutations(n, result, list(range(1, n + 1)), 0)
    return result


def _permutations(n, result, p, start):
    if start == n:
        result.append(tuple(p))
    else:
        next_index = start + 1
        _permutations(n, result, p, next_index)

        for i in range(next_index, n):
            p[i], p[start] = p[start], p[i]
            _permutations(n, result, p, next_index)
            p[i], p[start] = p[start], p[i]


def is_beautiful(index, num):
    if index == num:
        return True
    elif index > num:
        return index % num == 0
    else:
        return num % index == 0


# O(n!) time. O(n) space. Backtracking, recursive permutation.
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
