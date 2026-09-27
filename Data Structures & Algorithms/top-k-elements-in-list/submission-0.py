class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        #hash map store them key,value(frequecy) first
        #step1: count frequecy
        for num in nums:  # becuase nums is list, can directly start as num
            if num not in count:  
                count[num] = 1
            else:
                count[num] += 1
        sorted_nums = sorted(count, key=count.get, reverse=True)

        return sorted_nums[:k]

        
        
            