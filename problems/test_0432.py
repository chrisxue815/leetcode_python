import unittest

import sortedcontainers

import utils


class AllOne:

    def __init__(self):
        self.counts = {}
        self.keys = sortedcontainers.SortedDict()

    def inc(self, key: str) -> None:
        if key in self.counts:
            count = self.counts[key]
            keys = self.keys[count]
            keys.remove(key)
            if not keys:
                del self.keys[count]
            count += 1
        else:
            count = 1

        self.counts[key] = count

        if count in self.keys:
            keys = self.keys[count]
        else:
            self.keys[count] = keys = set()
        keys.add(key)

    def dec(self, key: str) -> None:
        count = self.counts[key]
        keys = self.keys[count]
        keys.remove(key)
        if not keys:
            del self.keys[count]
        count -= 1

        if count > 0:
            self.counts[key] = count
            if count in self.keys:
                keys = self.keys[count]
            else:
                self.keys[count] = keys = set()
            keys.add(key)
        else:
            del self.counts[key]

    def getMaxKey(self) -> str:
        return next(iter(self.keys.peekitem()[1])) if self.keys else ''

    def getMinKey(self) -> str:
        return next(iter(self.keys.peekitem(0)[1])) if self.keys else ''


class Test(unittest.TestCase):
    def test(self):
        utils.test_invocations(self, __file__, AllOne)


if __name__ == '__main__':
    unittest.main()
