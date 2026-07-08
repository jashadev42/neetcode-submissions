class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs)
        res = []
        count = 0
        check = True
        while count < len(smallest):
            temp = smallest[count]
            for word in strs:
                if word[count] != temp:
                    return "".join(res)
            res.append(temp)
            count += 1
        return "".join(res)