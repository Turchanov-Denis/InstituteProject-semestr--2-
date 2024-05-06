class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def logic(strt, tmp):
            res.append(tmp[:])
            for i in range(strt, len(nums)):
                tmp.append(nums[i])
                logic(i + 1, tmp)
                tmp.pop()
        res = []
        logic(0, []) 
        return res


if __name__ == "__main__":
    print(Solution().subsets([1, 2, 3]))
