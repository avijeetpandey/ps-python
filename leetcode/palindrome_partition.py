class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.st = s
        self.n = len(s)

        @cache # cache the result
        def isPalindrome(temp):
            return temp == temp[::-1]

        def choose(idx,existingParts):
            if idx >= self.n:
                self.res.append(existingParts.copy())
                return 

            for i in range(idx,self.n):
                tempSubstr = self.st[idx:i+1]
                if isPalindrome(tempSubstr):
                    existingParts.append(tempSubstr)
                    choose(i+1,existingParts)
                    existingParts.pop()

        emptyList = []     
        choose(0, emptyList)
        return self.res