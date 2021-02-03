class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        lst = list(s)
        temp = 0
        for i in s:
            char = i
            lst.pop(indices[temp])
            lst.insert(indices[temp], char)
            temp += 1
        finalstr = ''.join(lst)
        return finalstr

