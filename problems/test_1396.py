import unittest

import utils


# O(n) space. Hash table.
class UndergroundSystem:

    # O(1) time. O(1) space.
    def __init__(self):
        self.customers = {}
        self.times = {}

    # O(1) time. O(1) space.
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName, t)

    # O(1) time. O(1) space.
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, in_time = self.customers[id]
        pair = (start_station, stationName)
        if pair in self.times:
            time = self.times[pair]
        else:
            self.times[pair] = time = [0, 0]
        time[0] += t - in_time
        time[1] += 1

    # O(1) time. O(1) space.
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time = self.times[(startStation, endStation)]
        return time[0] / time[1]


class Test(unittest.TestCase):
    def test(self):
        utils.test_invocations(self, __file__, UndergroundSystem, check_result=self.check_result)

    def check_result(self, func, parameters, expected, actual, msg):
        if func == UndergroundSystem.getAverageTime.__name__:
            self.assertAlmostEqual(expected, actual, places=5, msg=msg)
        else:
            self.assertEqual(expected, actual, msg=msg)


if __name__ == '__main__':
    unittest.main()
