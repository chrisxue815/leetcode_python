import unittest

import sortedcontainers

import utils


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counts = {}
        self.keys = sortedcontainers.SortedDict()

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
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
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
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
        """
        Returns one of the keys with maximal value.
        """
        return next(iter(self.keys.peekitem()[1])) if self.keys else ''

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return next(iter(self.keys.peekitem(0)[1])) if self.keys else ''


class Test(unittest.TestCase):
    def test(self):
        utils.test_invocations(self, __file__, AllOne)


if __name__ == '__main__':
    unittest.main()
