class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i in range(len(nums)):
            look = target - nums[i]
            if look in result:
                return [result[look], i]
            result[nums[i]] = i


        