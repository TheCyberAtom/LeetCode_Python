class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sumdigit = 0
        while n != 0:
            temp = n % 10
            n //= 10
            prod *= temp
            sumdigit += temp
        return prod - sumdigit
