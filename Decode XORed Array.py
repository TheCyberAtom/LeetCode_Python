class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        lst = []
        lst.append(first)
        for i in encoded:
            temp = i ^ lst[-1]
            lst.append(temp)
        return lst
