"""
https://leetcode.com/problems/self-dividing-numbers/description/

https://leetcode.com/submissions/detail/129238510/
"""

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        numbers = []
        for num in range(left, right + 1):
            numStr = str(num)
            if '0' not in numStr:
                allDividing = True
                for char in numStr:
                    charNumber = int(char)
                    if num % charNumber != 0:
                        allDividing = False
                        break
                if allDividing:
                    numbers.append(num)
        return numbers



import unittest

class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.selfDividingNumbers(1, 22), [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])


if __name__ == '__main__':
    unittest.main()
