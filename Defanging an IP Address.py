class Solution:
    def defangIPaddr(self, address: str) -> str:
        lst = address.split('.')
        res = "[.]".join(lst)
        return res
