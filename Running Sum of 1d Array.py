class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[]
        temp=0
        for i in nums:
            temp+=i
            res.append(temp)
        return res