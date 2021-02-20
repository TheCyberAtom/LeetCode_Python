class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums_dict={}
        sum=0
        for i in nums:
            if i in nums_dict:
                nums_dict[i]+=1
            else:
                nums_dict[i]=1
        for k,v in nums_dict.items():
            if v==1:
                sum+=k
        return sum