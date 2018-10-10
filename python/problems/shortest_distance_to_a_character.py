"""
https://leetcode.com/problems/shortest-distance-to-a-character/description/

https://leetcode.com/submissions/detail/181688766/
"""


class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        ans = []
        dis = len(S)
        for char in S:
            if C == char:
                dis = 0
                ans.append(0)
            else:
                dis += 1
                ans.append(dis)
        dis = len(ans)
        for i in range(len(ans) - 1, -1, -1):
            if ans[i] == 0:
                dis = 0
            else:
                dis += 1
            ans[i] = min(ans[i], dis)
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.shortestToChar('loveleetcode', 'e'), [
                         3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0])


if __name__ == '__main__':
    unittest.main()
