class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        key = nums.pop()
        s=[]
        s.append(key)
        while(nums):
            i = nums.pop()
            s.append(i)
            if i < key:
                break
            key = i
        flag = 0
        for i in range(0, len(s)-1):
            if s[i] > s[len(s)-1]:
                flag = 1
                break
        if flag:        
            s[len(s)-1],s[i] = s[i],s[len(s)-1]
            nums.append(s.pop())
        while(s):
            nums.append(s.pop(0))
