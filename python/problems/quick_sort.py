"""


"""

from typing import List


def quickSort(A: List[int], start: int, end: int) -> List[int]:
    if start >= end:
        return A
    k = partition(A, start, end)
    quickSort(A, start, k - 1)
    quickSort(A, k + 1, end)
    return A


def partition(A: List[int], start: int, end: int) -> int:
    v, i, j = A[start], start, end
    while True:
        while True:
            if A[i] > v:
                break
            if i == end:
                break
            i += 1
        while True:
            if A[j] < v:
                break
            if j == start:
                break
            j -= 1
        if i >= j:
            break
        exchange(A, i, j)
    exchange(A, start, j) #! exchange start and j
    return j #! return pivot


def exchange(A: List[int], i: int, j: int):
    A[i], A[j] = A[j], A[i]


import unittest


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(quickSort([6, 2, 7, 3, 8, 9], 0, 5), [
            2, 3, 6, 7, 8, 9])
        self.assertEqual(quickSort([1, 6, 7, 3, 8, 9, 6], 0, 6), [
            1, 3, 6, 6, 7, 8, 9])
        self.assertEqual(quickSort([6, 4, 8, 2, 12, 5, 5, 2, 6, 1, 4, 4, 5, 6, 4, 1, 7, 3, 5, 10], 0, 19), [
            1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 8, 10, 12])


if __name__ == '__main__':
    unittest.main()
