class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxx = nums[0]
        minn = nums[0]
        ans = nums[0]
        if len(nums) == 1:
            return ans
        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxx, minn = minn, maxx
            maxx = max(maxx*nums[i], nums[i])
            minn = min(minn*nums[i], nums[i])
            ans = max(maxx, ans)
        return ans
