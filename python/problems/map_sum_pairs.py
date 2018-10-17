"""
https://leetcode.com/problems/map-sum-pairs/

https://leetcode.com/submissions/detail/131240001/
"""


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = dict()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.dic[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        result = 0
        for key, val in self.dic.items():
            if key.startswith(prefix):
                result += val
        return result


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


import unittest


class Test(unittest.TestCase):
    def test(self):
        mapSum = MapSum()
        mapSum.insert('apple', 3)
        self.assertEqual(mapSum.sum('ap'), 3)
        mapSum.insert('app', 2)
        self.assertEqual(mapSum.sum('ap'), 5)


if __name__ == '__main__':
    unittest.main()
