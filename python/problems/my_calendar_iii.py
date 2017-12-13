"""
https://leetcode.com/problems/my-calendar-iii/description/


"""


class MyCalendarThree:

    def __init__(self):
        self.timeSpan = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """

        return 1


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

import unittest


class Test(unittest.TestCase):
    def test(self):
        myCalendarThree = MyCalendarThree()
        self.assertEqual(myCalendarThree.book(10, 20), 1)


if __name__ == '__main__':
    unittest.main()
