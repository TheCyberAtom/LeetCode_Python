class Solution:
    def sumZero(self, n: int) -> List[int]:
        nums = []
        t1 = -1
        t2 = 1
        if n == 1:
            nums.append(0)
        elif n % 2 == 0:
            for i in range(n // 2):
                nums.append(t1)
                nums.append(t2)
                t1 -= 1
                t2 += 1
        else:
            nums.append(0)
            for i in range(n // 2):
                nums.append(t1)
                nums.append(t2)
                t1 -= 1
                t2 += 1
        return nums
