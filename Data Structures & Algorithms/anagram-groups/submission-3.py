from collections import Counter
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        grouped = set()                    # indices already placed
        for i in range(len(strs)):
            if i in grouped:
                continue
            chars_word = Counter(strs[i])
            pairs_temp = [strs[i]]
            grouped.add(i)                 # place the anchor itself
            for j in range(i + 1, len(strs)):
                if j not in grouped and Counter(strs[j]) == chars_word:
                    pairs_temp.append(strs[j])
                    grouped.add(j)
            res.append(pairs_temp)
        return res