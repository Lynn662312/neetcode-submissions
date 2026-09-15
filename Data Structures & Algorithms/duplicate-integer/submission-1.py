class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()  #set() is based on dict {} but only store value
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


        
        
        