class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=[]
        for i in range(0,len(nums)-2):
            low = i + 1
            hig = len(nums) - 1
            if(i > 0 and nums[i-1] == nums[i]):
                continue
            while(low < hig):
                if (nums[i] + nums[low] + nums[hig] > 0) and (low < hig):
                    hig = hig - 1
                elif (nums[i] + nums[low] + nums[hig] < 0) and (low < hig):
                    low = low + 1
                else:
                    ans.append([nums[i],nums[low],nums[hig]])
                    while(nums[low] == nums[low+1] and low+1 < hig):
                        low = low + 1
                    while(nums[hig] == nums[hig-1] and low < hig-1):
                        hig = hig - 1
                    low = low + 1
                    hig = hig - 1
        return ans
