class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        res = []
        for i in candies:
            if i + extraCandies < maxCandies:
                res.append(False)
            else:
                res.append(True)
        return res
