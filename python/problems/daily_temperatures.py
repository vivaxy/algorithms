"""
https://leetcode.com/problems/daily-temperatures/description/


"""


class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        temperaturesLength = len(temperatures)
        result = []
        for index in range(temperaturesLength):
            tem = temperatures[index]
            i = index + 1
            found = False
            while i < temperaturesLength:
                if temperatures[i] > tem:
                    found = True
                    break
                i += 1
            if found:
                result.append(i - index)
            else:
                result.append(0)
        return result


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(
            solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]),
            [1, 1, 4, 2, 1, 1, 0, 0]
        )


if __name__ == '__main__':
    unittest.main()
