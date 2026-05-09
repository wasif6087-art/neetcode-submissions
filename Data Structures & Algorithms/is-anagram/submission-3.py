class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars1 = sorted(list(s))
        chars2 = sorted(list(t))

        if chars1 == chars2 :

            return True
        return False

            