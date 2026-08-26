class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        num1 = sorted(s)
        num2 = sorted(t)

        if num1 == num2 :
            return True
        else :return False