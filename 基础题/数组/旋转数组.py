class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num1 = nums[0:len(nums) - k]
        num2 = nums[len(nums) - k:]
        nums[:] = num2 + num1