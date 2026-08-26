class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new = ""

        for j in s:
            if j.isalnum():
                new += j
        return new == new[::-1]