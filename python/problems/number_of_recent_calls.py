"""
https://leetcode.com/problems/number-of-recent-calls/

https://leetcode.com/submissions/detail/187528315/
"""


class RecentCounter:

    def __init__(self):
        self.t = []

    def findIndex(self, s, e, v):
        if e == s:
            return e
        if e - s == 1:
            if self.t[s] >= v:
                return s
            return e
        i = int((s + e) / 2)
        _v = self.t[i]
        if v > _v:
            return self.findIndex(i + 1, e, v)
        return self.findIndex(s, i, v)


    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        s = self.findIndex(0, len(self.t), t - 3000)
        e = self.findIndex(0, len(self.t), t)
        r = e - s + 1
        for i in range(e, len(self.t)):
            if self.t[i] == t:
                r += 1
        self.t.insert(e, t)
        return r



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


import unittest


class Test(unittest.TestCase):
    def test(self):
        obj = RecentCounter()
        param_1 = obj.ping(1)
        self.assertEqual(param_1, 1)
        param_2 = obj.ping(100)
        self.assertEqual(param_2, 2)
        param_3 = obj.ping(3001)
        self.assertEqual(param_3, 3)
        param_4 = obj.ping(3002)
        self.assertEqual(param_4, 3)


if __name__ == '__main__':
    unittest.main()
