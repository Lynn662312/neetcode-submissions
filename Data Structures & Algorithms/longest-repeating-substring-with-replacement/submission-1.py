class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        best_length = 0
        maxf = 0

        for right in range(len(s)):
            # dict/map is (key:value)
            #dict[key] = value , dict.get(key,default value)
            freq[s[right]] = 1+ freq.get(s[right],0)
            maxf = max(maxf,freq[s[right]])
            
            while (right-left + 1) - maxf > k:
                freq[s[left]] -=1
                left +=1
            best_length = max(best_length, right-left+1)
        return best_length
        