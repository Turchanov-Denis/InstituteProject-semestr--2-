class Solution:
    def missingNumber(self, nums: list[int]):
        for i,j in enumerate(sorted(nums)):
            if i!=j:
                return i
        return len(nums)
    
nums=[0,1]
test = Solution()
print(test.missingNumber(nums))
# missing = len(mums)
# missing ^=i^j