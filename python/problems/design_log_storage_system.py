"""
https://leetcode.com/problems/design-log-storage-system/

https://leetcode.com/submissions/detail/108885654/
"""


class LogSystem(object):

    def __init__(self):
        self.logs = []

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        lb = self.bsLower(0, len(self.logs) - 1, timestamp, 'Second')
        if lb > len(self.logs) - 1:
            return self.logs.append([id, timestamp])
        if self.compare(self.logs[lb][1], timestamp, 'Second') > 0:
            lb += 1
        if lb > len(self.logs) - 1:
            return self.logs.append([id, timestamp])
        return self.logs.insert(lb, [id, timestamp])

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        if len(self.logs) == 0:
            return []
        slb = self.bsLower(0, len(self.logs) - 1, s, gra)
        ehb = self.bsHigher(slb, len(self.logs) - 1, e, gra)
        if slb == ehb and self.compare(self.logs[slb][1], e, gra) < 0:
            return []
        if slb == ehb and self.compare(self.logs[slb][1], s, gra) > 0:
            return []
        return list(sorted(map(lambda x: x[0], self.logs[slb:ehb + 1])))

    def bsLower(self, startIndex, endIndex, ts, gra):
        # get first met index
        if endIndex - startIndex < 0:
            return 0
        if endIndex - startIndex < 2:
            if self.compare(self.logs[startIndex][1], ts, gra) <= 0:
                return startIndex
            return endIndex
        mid = int((startIndex + endIndex) / 2)
        if self.compare(self.logs[mid][1], ts, gra) > 0:
            return self.bsLower(mid, endIndex, ts, gra)
        return self.bsLower(startIndex, mid, ts, gra)

    def bsHigher(self, startIndex, endIndex, ts, gra):
        # get last met index
        if endIndex - startIndex < 0:
            return 0
        if endIndex - startIndex < 2:
            if self.compare(self.logs[endIndex][1], ts, gra) >= 0:
                return endIndex
            return startIndex
        mid = int((startIndex + endIndex) / 2)
        if self.compare(self.logs[mid][1], ts, gra) < 0:
            return self.bsHigher(startIndex, mid, ts, gra)
        return self.bsHigher(mid, endIndex, ts, gra)

    def compare(self, base, ts, gra):
        [YearBase, MonthBase, DayBase, HourBase,
            MinuteBase, SecondBase] = base.split(':')
        [Year, Month, Day, Hour, Minute, Second] = ts.split(':')
        if gra == 'Year':
            return int(Year) - int(YearBase)
        elif gra == 'Month':
            return int(Year + Month) - int(YearBase + MonthBase)
        elif gra == 'Day':
            return int(Year + Month + Day) - int(YearBase + MonthBase + DayBase)
        elif gra == 'Hour':
            return int(Year + Month + Day + Hour) - int(YearBase + MonthBase + DayBase + HourBase)
        elif gra == 'Minute':
            return int(Year + Month + Day + Hour + Minute) - int(YearBase + MonthBase + DayBase + HourBase + MinuteBase)
        return int(Year + Month + Day + Hour + Minute + Second) - int(YearBase + MonthBase + DayBase + HourBase + MinuteBase + SecondBase)


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)


import unittest


class Test(unittest.TestCase):
    def test(self):
        # logSystem1 = LogSystem()
        # logSystem1.put(1, "2017:01:01:23:59:59")
        # logSystem1.put(2, "2017:01:01:22:59:59")
        # logSystem1.put(3, "2016:01:01:00:00:00")
        # self.assertEqual(logSystem1.retrieve(
        #     "2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"), [1, 2, 3])
        # self.assertEqual(logSystem1.retrieve(
        #     "2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"), [1, 2])

        # logSystem2 = LogSystem()
        # logSystem2.put(1, "2017:01:01:23:59:59")
        # logSystem2.put(2, "2017:01:02:23:59:59")
        # self.assertEqual(logSystem2.retrieve(
        #     "2017:01:01:23:59:58", "2017:01:02:23:59:58", "Second"), [1])

        logSystem3 = LogSystem()
        logSystem3.put(1,"2005:01:05:22:16:15")
        logSystem3.put(2,"2003:12:12:20:30:51")
        self.assertEqual(logSystem3.retrieve(
            "2005:07:10:17:43:43","2007:02:18:10:22:52","Month"), [])

if __name__ == '__main__':
    unittest.main()
