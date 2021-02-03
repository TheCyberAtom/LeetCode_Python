class Solution:
    def interpret(self, command: str) -> str:
        res=[]
        lst=list(command)
        for i in range(len(lst)):
            if lst[i]=='G':
                res.append('G')
            elif lst[i]=='(' and lst[i+1]==')':
                res.append('o')
            elif lst[i]=='(' and lst[i+1]=='a':
                res.append('al')
        parsed=''.join(res)
        return parsed