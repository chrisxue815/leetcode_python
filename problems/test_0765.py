import unittest
import utils


# O(n) time. O(n) space. Greedy.
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        seats = [0] * len(row)
        for seat, person in enumerate(row):
            seats[person] = seat

        count = 0

        for seat_a in range(0, len(row), 2):
            person_a = row[seat_a]
            person_b = row[seat_a + 1]
            person_c = ((person_b >> 1) << 2) + 1 - person_b
            if person_a != person_c:
                count += 1
                seat_c = seats[person_c]
                row[seat_a], row[seat_c] = person_c, person_a
                seats[person_a], seats[person_c] = seat_c, seat_a

        return count


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().minSwapsCouples(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
