"""
https://leetcode.com/problems/my-calendar-iii/

https://leetcode.com/submissions/detail/139013850/
"""

import collections


class MyCalendarThree:

    def __init__(self):
        self.delta = collections.Counter()

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        self.delta[start] += 1
        self.delta[end] -= 1
        active = 0
        ans = 0
        for x in sorted(self.delta):
            active += self.delta[x]
            if active > ans:
                ans = active
        return ans


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

import unittest


class Test(unittest.TestCase):
    def test(self):
        myCalendarThree = MyCalendarThree()
        self.assertEqual(myCalendarThree.book(10, 20), 1)
        self.assertEqual(myCalendarThree.book(50, 60), 1)
        self.assertEqual(myCalendarThree.book(10, 40), 2)
        self.assertEqual(myCalendarThree.book(5, 15), 3)
        self.assertEqual(myCalendarThree.book(5, 10), 3)
        self.assertEqual(myCalendarThree.book(25, 55), 3)


if __name__ == '__main__':
    unittest.main()
