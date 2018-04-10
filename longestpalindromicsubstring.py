class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        for i in self.frange(0, len(s), 0.5):
            check = 0.4      
            while(i-check > 0 and i+check < len(s)):
                if s[int(i-check)] == s[int(i+check)]:
                    check = check+1
                else:
                    break
            if int(i+check-1)+1-int(i-check+1) > len(ans) :
                ans = s[int(i-check+1):int(i+check-1)+1]
        return ans
    
    def frange(self, be, end, jump):
        while be < end:
            yield be
            be += jump
