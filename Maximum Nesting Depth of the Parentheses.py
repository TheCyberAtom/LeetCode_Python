class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxcount = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
            if maxcount < count:
                maxcount = count
        return maxcount
