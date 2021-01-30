class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        finalList=[]
        for i in range(0,len(nums),2):
            for j in range(nums[i]):
                finalList.append(nums[i+1])
        return finalList