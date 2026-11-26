class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {} #key, value
        for i,num in enumerate(nums):
            needed= target - num
            if needed in result:
                return [result[needed],i]
            result[nums[i]] = i

        