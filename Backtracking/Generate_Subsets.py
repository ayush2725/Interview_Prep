class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def back(curr, i):
            if len(curr) == len(nums):
                ans.append(curr)
            else:
                ans.append(curr)
                for i in range(i, len(nums)):
                    back(curr + [nums[i]], i + 1)
        back([], 0)
        return ans
