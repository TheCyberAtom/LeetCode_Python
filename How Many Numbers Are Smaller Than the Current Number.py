class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst = sorted(nums)
        res = []
        for i in nums:
            for j in range(len(lst)):
                if i == lst[j]:
                    res.append(j)
                    break
        return res


