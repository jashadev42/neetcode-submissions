from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_s = Counter(s)
        chars_t = Counter(t)

        if chars_s == chars_t:
            return True
        return False