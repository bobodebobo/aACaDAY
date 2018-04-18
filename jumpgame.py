class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag = len(nums)
        if flag == 1:
            return True
        while(flag != 1):
            for i in range(flag-2, -1, -1):
                if i + nums[i] >= flag-1:
                    break
            if i == 0 and nums[0] < flag-1:
                return False
            flag = i+1
        return True
        
