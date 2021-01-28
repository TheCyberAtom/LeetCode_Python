class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res=0
        for i in accounts:
            if sum(i)>=res:
                res=sum(i)
        return res