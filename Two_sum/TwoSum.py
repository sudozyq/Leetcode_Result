class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        # 将{nums[i] : i} 加入字典
        # 如果匹配到了target - nums[i]在字典中，说明此时nums[i] + 内部匹配值 = target
        # 返回这对key
        for i in range(len(nums)):
            if target - nums[i] not in nums_dict:
                nums_dict[nums[i]] = i
            else:
                return [nums_dict[target - nums[i]], i]