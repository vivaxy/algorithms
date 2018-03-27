"""
https://leetcode.com/problems/unique-morse-code-words/description/

https://leetcode.com/submissions/detail/147142806/
"""


class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morseCode = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                     "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        return len(set(map(lambda word: ''.join([morseCode[ord(letter) - 97] for letter in word]), words)))


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.uniqueMorseRepresentations(
            ["gin", "zen", "gig", "msg"]), 2)


if __name__ == '__main__':
    unittest.main()
