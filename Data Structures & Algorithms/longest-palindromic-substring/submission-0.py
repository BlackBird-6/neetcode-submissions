class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = "".join([c + "-" for c in s])
        
        res = ""
        for i in range(len(s)):
            for dx in range(i+1):
                if i-dx >= 0 and i+dx < len(s) and s[i+dx] == s[i-dx]:
                    if 2*dx+1 > len(res):
                        res = s[i-dx:i+dx+1]
                else:
                    break
        return res.replace("-", "")