"""
https://leetcode.com/problems/subdomain-visit-count/

https://leetcode.com/submissions/detail/148073410/
"""


class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dic = dict()
        for cpdomain in cpdomains:
            [count, domain] = cpdomain.split(' ')
            count = int(count)
            domains = domain.split('.')
            domain = ''
            for index in range(len(domains)):
                domain = '.'.join(domains[index:])
                if (domain not in dic):
                    dic[domain] = 0
                dic[domain] += count
        ans = []
        for domain in dic:
            ans.append(str(dic[domain]) + ' ' + domain)
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.subdomainVisits(["9001 discuss.leetcode.com"]), [
                         "9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"])


if __name__ == '__main__':
    unittest.main()
