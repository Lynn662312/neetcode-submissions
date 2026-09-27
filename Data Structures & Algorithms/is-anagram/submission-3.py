# ord('a') is 97
# 用对称，1+1— 这样如果两个都有共同数字
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for val in count:
            if val != 0:
                return False  # because if anagram is 0 since all alphabet already simunatenously + -
        return True
        