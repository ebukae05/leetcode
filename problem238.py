class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = []
        prefix = 1
        suffix = 1
        for i in range(n):
            result.append(1)

        for i, x in enumerate(nums):
            result[i] = prefix
            prefix *= x

        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result