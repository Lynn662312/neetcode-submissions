class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newList = {}
        for i, n in enumerate(nums):
            needed = target - n
            if needed in newList:
                return [newList[needed],i]
            newList[n] = i
        