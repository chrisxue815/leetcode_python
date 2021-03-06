import random
import unittest


def binary_search(a, x, lo=0, hi=-1):
    n = len(a)
    if hi < 0:
        hi += n

    # See OpenJDK Arrays.binarySearch0():
    # https://github.com/openjdk/jdk/blob/f37d9c8abca50b65ed232831a06d60c1d015013f/src/java.base/share/classes/java/util/Arrays.java#L1829
    # See CoreCLR ArrayHelpers::BinarySearchBitwiseEquals():
    # https://github.com/dotnet/coreclr/blob/310c1903838f048afc66121212342e0d55b50d11/src/classlibnative/bcltype/arrayhelpers.h#L62
    # See CPython bisect.bisect_right():
    # https://github.com/python/cpython/blob/898318b53d921298d1f1fcfa0f415844afbeb318/Lib/bisect.py#L15
    while lo <= hi:
        mid = lo + ((hi - lo) >> 1)
        mid_val = a[mid]
        if mid_val < x:
            lo = mid + 1
        elif mid_val > x:
            hi = mid - 1
        else:
            return mid
    return ~lo


def binary_search_rightmost(a, x, left=0, right=-1):
    """
    Returns the index of the rightmost x's right neighbor.
    arg->right is inclusive.
    """
    n = len(a)
    if right < 0:
        right += n

    while left <= right:
        mid = left + (right - left) // 2
        if x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return left


def binary_insert(a, x, left=0, right=-1):
    n = len(a)
    if right < 0:
        right += n

    index = binary_search_rightmost(a, x, left, right)
    a[index + 1: right + 2] = a[index: right + 1]
    a[index] = x


# Insertion

def insertion_sort(a):
    # See OpenJDK Arrays.mergeSort(), Insertion sort on smallest arrays:
    # https://github.com/openjdk/jdk/blob/f37d9c8abca50b65ed232831a06d60c1d015013f/src/java.base/share/classes/java/util/Arrays.java#L1349
    # See CoreCLR ArrayHelpers::InsertionSort():
    # https://github.com/dotnet/coreclr/blob/310c1903838f048afc66121212342e0d55b50d11/src/classlibnative/bcltype/arrayhelpers.h#L282
    n = len(a)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if a[j - 1] <= a[j]:
                break
            a[j - 1], a[j] = a[j], a[j - 1]


def insertion_sort_memmove(a):
    n = len(a)
    for i in range(1, n):
        next_val = a[i]
        j = i - 1
        while j >= 0 and a[j] > next_val:
            j -= 1
        # memmove(a + j + 1, a + j, i - j)
        a[j + 2: i + 1] = a[j + 1: i]
        a[j + 1] = next_val


def binary_insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        binary_insert(a, a[i], 0, i - 1)


def _shell_gaps(n):
    gap = n // 2
    while gap > 0:
        yield gap
        gap //= 2


def shell_sort(a):
    n = len(a)
    for gap in _shell_gaps(n):
        for i in range(gap, n):
            to_be_inserted = a[i]
            j = i
            while j >= gap and a[j - gap] > to_be_inserted:
                a[j] = a[j - gap]
                j -= gap
            a[j] = to_be_inserted


# Swap

def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(1, n - i):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]


def _quick_sort(a, left, right):
    if left >= right:
        return
    middle = left + (right - left) // 2
    pivot = a[middle]
    i = left
    j = right
    while i <= j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i > j:
            break
        elif i < j:
            a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    # Optimization: tail call
    # See CLR ArrayHelpers::QuickSort():
    # https://github.com/kasicass/sscli20/blob/dc64e12c9b835d4d373aa04978c0e8f1763b2e1b/clr/src/vm/comarrayhelpers.h#L77
    # See CLR ArraySortHelper.QuickSort():
    # https://github.com/kasicass/sscli20/blob/dc64e12c9b835d4d373aa04978c0e8f1763b2e1b/clr/src/bcl/system/collections/generic/arraysorthelper.cs#L70
    _quick_sort(a, left, j)
    _quick_sort(a, i, right)


def quick_sort(a):
    _quick_sort(a, 0, len(a) - 1)


# Selection

def selection_sort(a):
    n = len(a)
    for i in range(n):
        min_val = a[i]
        min_val_index = i
        for j in range(i + 1, n):
            if a[j] < min_val:
                min_val = a[j]
                min_val_index = j
        a[i], a[min_val_index] = a[min_val_index], a[i]


# Merging

def _merge_sort(dest, src, low, high):
    # Optimization: using insertion sort on smallest arrays (length < 7)
    # See OpenJDK Arrays.mergeSort():
    # https://github.com/openjdk/jdk/blob/f37d9c8abca50b65ed232831a06d60c1d015013f/src/java.base/share/classes/java/util/Arrays.java#L1342
    if low >= high - 1:
        return

    mid = low + (high - low) // 2
    _merge_sort(src, dest, low, mid)
    _merge_sort(src, dest, mid, high)

    if src[mid - 1] < src[mid]:
        dest[low: high] = src[low: high]
        return

    p = low
    q = mid
    for i in range(low, high):
        if q >= high or p < mid and src[p] < src[q]:
            dest[i] = src[p]
            p += 1
        else:
            dest[i] = src[q]
            q += 1


def merge_sort(a):
    aux = list(a)
    _merge_sort(a, aux, 0, len(a))


def merge_sort_iterative(a):
    n = len(a)
    aux = [0] * n

    sublen = 1  # sublist length
    while True:
        new_sublen = sublen << 1  # new sublist length after merge

        for lo in range(0, n, new_sublen):
            lo_end = min(lo + sublen, n)
            hi = lo_end
            hi_end = min(hi + sublen, n)

            for i in range(lo, hi_end):
                if hi >= hi_end or lo < lo_end and a[lo] <= a[hi]:
                    aux[i] = a[lo]
                    lo += 1
                else:
                    aux[i] = a[hi]
                    hi += 1

        if new_sublen >= n:
            break
        sublen = new_sublen
        a, aux = aux, a

    return aux


# Misc

def _down_heap(a, root, n):
    while True:
        child = 2 * root + 1
        if child >= n:
            break

        # find the larger child
        if child + 1 < n and a[child] < a[child + 1]:
            child += 1

        if a[child] <= a[root]:
            break

        a[root], a[child] = a[child], a[root]
        root = child


def heap_sort(a):
    # See CoreCLR ArrayHelpers::Heapsort():
    # https://github.com/dotnet/coreclr/blob/310c1903838f048afc66121212342e0d55b50d11/src/classlibnative/bcltype/arrayhelpers.h#L242
    # See OpenJDK PriorityQueue.heapify():
    # https://github.com/openjdk/jdk/blob/f37d9c8abca50b65ed232831a06d60c1d015013f/src/java.base/share/classes/java/util/PriorityQueue.java#L724
    # See CPython heapq.heapify():
    # https://github.com/python/cpython/blob/898318b53d921298d1f1fcfa0f415844afbeb318/Lib/heapq.py#L168
    n = len(a)

    for i in range(n // 2 - 1, -1, -1):
        _down_heap(a, i, n)

    for i in range(n - 1, -1, -1):
        a[0], a[i] = a[i], a[0]
        _down_heap(a, 0, i)


def radix_sort(a):
    # See com.indeed.util.core.sort.RadixSort.radixSort():
    # https://github.com/indeedeng/util/blob/2e640a121abfcc6fad6947baeb7adecee1dc50ca/util-core/src/main/java/com/indeed/util/core/sort/RadixSort.java#L7
    n = len(a)
    count_scratch = [0] * 0x10000
    scratch = [0] * n
    sum_ = 0
    for num in a:
        radix = num & 0xFFFF
        count_scratch[radix] += 1
    for i in range(0x10000):
        tmp = count_scratch[i]
        count_scratch[i] = sum_
        sum_ += tmp
    for i in range(n):
        num = a[i]
        radix = num & 0xFFFF
        offset = count_scratch[radix]
        scratch[offset] = a[i]
        count_scratch[radix] += 1

    count_scratch = [0] * 0x10000
    sum_ = 0
    for num in a:
        radix = (num >> 16) + 0x8000
        count_scratch[radix] += 1
    for i in range(0x10000):
        tmp = count_scratch[i]
        count_scratch[i] = sum_
        sum_ += tmp
    for i in range(n):
        num = scratch[i]
        radix = (num >> 16) + 0x8000
        offset = count_scratch[radix]
        a[offset] = scratch[i]
        count_scratch[radix] += 1


class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)

        start = -5
        end = 5
        self.ordered = list(range(start, end))

        cloned = list(self.ordered)
        random_func = random.Random(1).random
        random.shuffle(cloned, random_func)
        self.unordered = cloned

    def test(self):
        self._test(insertion_sort)
        self._test(insertion_sort_memmove)
        self._test(binary_insertion_sort)
        self._test(shell_sort)
        self._test(bubble_sort)
        self._test(quick_sort)
        self._test(selection_sort)
        self._test(merge_sort)
        self._test(merge_sort_iterative)
        self._test(heap_sort)
        self._test(radix_sort)

    def _test(self, func):
        unordered = list(self.unordered)
        func(unordered)
        self.assertEqual(self.ordered, unordered)


if __name__ == '__main__':
    unittest.main()
