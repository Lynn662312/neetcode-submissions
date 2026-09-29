class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        freq = [[] for i in range(len(nums)+1)]
        # +1 是因为the num may appear from 0 until len(nums) range , example have 7 num but some of the num may 0, some 7. using range(7) it only 0-6
        for num in nums:
            count[num] = 1 + count.get(num,0)
            # using count.get() will get the value, if doesnt have, add it as the key and the default value is 0
        for num,cnt in count.items():
            freq[cnt].append(num)
            #cnt is frequency (value)
#this will be the index of the freq (since default just create array but doesnt have any value inside) append the num
#the list index act as frequency, inside the specific list mean the num appear how many times
        res = []
        for i in range(len(freq)-1,0,-1):
            #if using len(Freq) it will start from higher frequency
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                
        