'''
Question:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses

Solution:
This can be achieved through top-down recursion. We keep a track of the current number of open and close 
parans. If the number of open is less than n, we recurse with open + 1. If close is less than open, we 
recurse with close + 1.

Corner Cases:
Can n be 0 or negative?

Time Complexity: O(4^n) // 2 digits (7 and 9) have 4 letters associated, in worse case, all the digits will either be 7 or 9. n is size of digits.
Space Compleity: O(n) // n is the size of digits, the stack will only go as deep as the number of digits
'''

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
        
