class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxx = 0
        tmpStr = set()
        if len(s) == 1:
            return 1
        for i in range(0,len(s)-1):
            tmpm = 0
            while(1):
                if s[i] not in tmpStr :
                    tmpStr.add(s[i])
                    tmpm = tmpm + 1
                    i = i + 1
                    if i == len(s):
                        break
                else:
                    tmpStr.clear()
                    break
            if tmpm > maxx:
                maxx = tmpm
        return maxx
