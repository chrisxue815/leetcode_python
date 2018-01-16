import unittest


def count_ones(num):
    count = 0
    while num != 0:
        if num & 1 == 1:
            count += 1
        num >>= 1
    return count


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        one_count_to_hours = [[] for _ in xrange(11)]
        for i in xrange(12):
            one_count_to_hours[count_ones(i)].append(i)

        one_count_to_minutes = [list(hours) for hours in one_count_to_hours]
        for i in xrange(12, 60):
            one_count_to_minutes[count_ones(i)].append(i)

        result = []
        for hour_ones in xrange(num + 1):
            minute_ones = num - hour_ones
            for hour in one_count_to_hours[hour_ones]:
                for minute in one_count_to_minutes[minute_ones]:
                    result.append('{}:{:02d}'.format(hour, minute))
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test(1, ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"])
        self._test(2, ["0:03", "0:05", "0:06", "0:09", "0:10", "0:12", "0:17", "0:18", "0:20", "0:24", "0:33", "0:34",
                       "0:36", "0:40", "0:48", "1:01", "1:02", "1:04", "1:08", "1:16", "1:32", "2:01", "2:02", "2:04",
                       "2:08", "2:16", "2:32", "3:00", "4:01", "4:02", "4:04", "4:08", "4:16", "4:32", "5:00", "6:00",
                       "8:01", "8:02", "8:04", "8:08", "8:16", "8:32", "9:00", "10:00"])

    def _test(self, num, expected):
        actual = Solution().readBinaryWatch(num)
        self.assertItemsEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
