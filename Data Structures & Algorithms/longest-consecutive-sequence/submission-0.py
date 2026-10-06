class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        setNum = set(nums)
        nums_list = sorted(setNum)
        longest = 1
        streak = 1
        i = 1
        while i < len(nums_list):
            if nums_list[i] == nums_list[i-1] + 1:
                streak +=1
            else:
                streak = 1
            longest = max(longest,streak)
            i +=1
        return longest

