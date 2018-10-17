"""
https://leetcode.com/problems/groups-of-special-equivalent-strings/

https://leetcode.com/submissions/detail/181442598/
"""


class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def hashifyString(str):
            a = []
            b = []
            i = 0
            for char in str:
                if i % 2 == 0:
                    a.append(char)
                else:
                    b.append(char)
                i += 1
            return ''.join(sorted(a)) + ',' + ''.join(sorted(b))
        mem = dict()
        for str in A:
            hash = hashifyString(str)
            if hash in mem:
                mem[hash].append(str)
            else:
                mem[hash] = []
        return len(mem)


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.numSpecialEquivGroups(
            ["a", "b", "c", "a", "c", "c"]), 3)
        self.assertEqual(solution.numSpecialEquivGroups(
            ["aa", "bb", "ab", "ba"]), 4)
        self.assertEqual(solution.numSpecialEquivGroups(
            ["abc", "acb", "bac", "bca", "cab", "cba"]), 3)
        self.assertEqual(solution.numSpecialEquivGroups(
            ["abcd", "cdab", "adcb", "cbad"]), 1)


if __name__ == '__main__':
    unittest.main()
