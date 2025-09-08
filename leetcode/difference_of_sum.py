class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        numOne = 0
        numTwo = 0
        for i in range(1,n+1):
            if i%m==0:
                numTwo+=i
            else:
                numOne+=i
        return numOne - numTwo