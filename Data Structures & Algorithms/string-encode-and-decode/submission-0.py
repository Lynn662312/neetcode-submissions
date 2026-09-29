class Solution:

    def encode(self, strs: List[str]) -> str:
        res =""
        for s in strs:
            res += str(len(s)) + "#" +s
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i =0
        while i<len(s):  #if empty list return
            j = i
            #get the length first, bfr the #
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  #just until bfr j
            i = j + 1 #move the i to the str

            word = s[i:i+length]
            res.append(word)
            #move to next encode string
            i = i + length 
        return res

