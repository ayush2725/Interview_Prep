class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def back(curr):
            if len(curr) == len(nums):
                ans.append(curr)
            else:
                for i in nums:
                    if i not in curr:
                        back(curr + [i])
        back([])
        return ans
