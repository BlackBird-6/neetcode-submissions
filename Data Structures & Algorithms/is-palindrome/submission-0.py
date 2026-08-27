class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        check = "".join([c if c in "abcdefghijklmnopqrstuvwxyz0123456789" else "" for c in s])
        return check == check[::-1]
        