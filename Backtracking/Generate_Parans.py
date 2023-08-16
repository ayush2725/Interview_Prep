class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def back(curr, o, c):
            if len(curr) == n*2:
                ans.append(curr)
                return
            if o < n:
                back(curr + "(", o + 1, c)
            if c < o:
                back(curr + ')', o, c + 1)
        back('', 0, 0)
        return ans
        
