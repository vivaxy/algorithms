"""
https://leetcode.com/problems/top-k-frequent-elements/

https://leetcode.com/submissions/detail/107591169/
"""


def quickSort(a, start, end):
    i = start
    j = end
    k = a[i]
    while i < j:
        while i < j and k['count'] <= a[j]['count']:
            j -= 1
        temp = a[j]
        a[j] = k
        a[i] = temp
        while i < j and k['count'] >= a[i]['count']:
            i += 1
        temp = a[i]
        a[i] = k
        a[j] = temp
    if start < i - 1:
        quickSort(a, start, i - 1)
    if end > i + 1:
        quickSort(a, i + 1, end)
    return a


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = dict()
        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
        uniqueNums = []
        for num in dic.keys():
            uniqueNums.append({'value': num, 'count': dic[num]})
        quickSort(uniqueNums, 0, len(uniqueNums) - 1)
        result = []
        for i in range(len(uniqueNums) - 1, len(uniqueNums) - k - 1, -1):
            result.append(uniqueNums[i]['value'])
        return result


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
        self.assertEqual(solution.topKFrequent(
            [4, 1, -1, 2, -1, 2, 3], 2), [2, -1])


if __name__ == '__main__':
    unittest.main()
