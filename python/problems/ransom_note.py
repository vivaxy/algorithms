"""
https://leetcode.com/problems/ransom-note/

https://leetcode.com/submissions/detail/108015385/
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        index = 0
        ransomNoteLen = len(ransomNote)
        while index < ransomNoteLen:
            char = ransomNote[index]
            magazineIndex = 0
            magazineLen = len(magazine)
            found = False
            while magazineIndex < magazineLen:
                mChar = magazine[magazineIndex]
                if mChar == char:
                    found = True
                    magazine = magazine[:magazineIndex] + magazine[magazineIndex + 1:]
                    break
                else:
                    magazineIndex += 1
            if found == False:
                return False
            index += 1
        return True

import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.canConstruct('a', 'b'), False)
        self.assertEqual(solution.canConstruct('aa', 'ab'), False)
        self.assertEqual(solution.canConstruct('aa', 'aab'), True)


if __name__ == '__main__':
    unittest.main()
