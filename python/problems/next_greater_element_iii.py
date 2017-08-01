"""
https://leetcode.com/problems/next-greater-element-iii/

https://leetcode.com/submissions/detail/111971825/
"""


class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        strNList = list(str(n))
        index = len(strNList) - 2
        remainingList = []
        while index >= 0:
            prevDigit = int(strNList[index])
            nextDigit = int(strNList[index + 1])
            if prevDigit < nextDigit:
                remainingList.append(str(nextDigit))
                # find next greater than prevDigit
                # put next greater in index
                # sort rest
                # join and return
                for i, d in enumerate(remainingList):
                    if int(d) > prevDigit:
                        break
                remainingList[i] = str(prevDigit)
                result =  int(''.join(strNList[:index]) + d + ''.join(remainingList))
                if result > 2 ** 31:
                    return -1
                return result
            remainingList.append(str(nextDigit))
            index -= 1
        return -1


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.nextGreaterElement(2147483647), -1)
        self.assertEqual(solution.nextGreaterElement(12443322), 13222344)
        self.assertEqual(solution.nextGreaterElement(12), 21)
        self.assertEqual(solution.nextGreaterElement(21), -1)


if __name__ == '__main__':
    unittest.main()
