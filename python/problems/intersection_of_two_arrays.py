"""
https://leetcode.com/problems/intersection-of-two-arrays/

https://leetcode.com/submissions/detail/107857447/
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.intersection([1, 2, 2, 1], [2, 2]), [2])


if __name__ == '__main__':
    unittest.main()
