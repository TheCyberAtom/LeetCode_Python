class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res=0
        for ele in nums:
            count=0
            while(ele!=0):
                ele//=10
                count+=1
            if count%2==0:
                res+=1
        return res