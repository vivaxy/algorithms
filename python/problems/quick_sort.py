"""


"""


def quickSort(a, start, end):
    """
    :type a: List[int]
    :type start: int
    :type end: int
    "rtype: List[int]
    """
    i = start
    j = end
    k = a[i]
    print('group: a = ' + str(a) + ', start = ' +
          str(start) + ', end = ' + str(end))

    print('    step: from j = ' + str(j) +
          ' to start, find the first item lower than k = ' + str(k))
    while i < j:
        while i < j and k <= a[j]:
            print('        j = ' + str(j) + ', a[j] = ' + str(a[j]))
            j -= 1
        temp = a[j]
        a[j] = k
        a[i] = temp
        print('        switch k and a[j]: i = ' +
            str(i) + ', j = ' + str(j) + ', a = ' + str(a))

        print('    step: from i = ' + str(i) +
            ' to end, find the first item greater than k = ' + str(k))
        while i < j and k >= a[i]:
            print('        i = ' + str(i) + ', a[i] = ' + str(a[i]))
            i += 1
        temp = a[i]
        a[i] = k
        a[j] = temp
        print('        switch k and a[i]: i = ' +
            str(i) + ', j = ' + str(j) + ', a = ' + str(a))
    print('group end: i = ' + str(i) + ', j = ' + str(j) + ' meets')
    if start < i - 1:
        quickSort(a, start, i - 1)
    if end > i + 1:
        quickSort(a, i + 1, end)
    return a


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
