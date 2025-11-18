class Solution:
    def defangIPaddr(self, address: str) -> str:
        lt = list(address)
        for i in range(0,len(lt)-1):
            if lt[i] == '.':
                lt[i] = '[.]'
        
        return ''.join(lt)