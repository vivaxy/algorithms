"""
https://leetcode.com/problems/my-calendar-iii/description/


"""


class MyCalendarThree:

    def __init__(self):
        self.timeSpan = []
        self.k = 1

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        for i in range(len(self.timeSpan), start):
            self.timeSpan.append(0)
        for i in range(start, min(end, len(self.timeSpan))):
            self.timeSpan[i] += 1
            if self.k < self.timeSpan[i]:
                self.k = self.timeSpan[i]
        for i in range(len(self.timeSpan), end):
            self.timeSpan.append(1)
        return self.k


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
