class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        q = []
        res = ""
        for c in s:
            if c == "(":
                q.append(c)
            if len(q) > 1:
                res += c

            if c == ")":
                q.pop()

        return res