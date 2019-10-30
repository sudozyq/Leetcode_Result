class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
            print(nums[i])
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        while k < len(nums):
            nums[k] = 0
            k += 1