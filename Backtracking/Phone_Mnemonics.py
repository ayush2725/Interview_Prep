'''
Question:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that 
the number could represent. Return the answer in any order.

Solution:
This can be achieved through top-down recursion. We keep a track of the current index that we're at 
in the given input. To the current string that we have, we add all the possible chars given the index
and call the function again

Corner Cases:
Does the input have the number '1'? If yes, would that be blank in combinations?

Time Complexity: O(4^n) // 2 digits (7 and 9) have 4 letters associated, in worse case, all the digits will either be 7 or 9. n is size of digits.
Space Compleity: O(n) // n is the size of digits, the stack will only go as deep as the number of digits
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        ans = []
      
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
      
        def back(curr, i):
            if len(curr) == len(digits):
                ans.append(curr)
            else:
                for key in letters[digits[i]]:
                    back(curr + key, i + 1)
        back('', 0)
        return ans
