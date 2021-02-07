class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr=0
        res=0
        for ele in gain:
            curr+=ele
            res=max(curr,res)
        return res