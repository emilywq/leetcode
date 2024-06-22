class Solution():
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        for x in range(1, len(nums)):
            if nums[x] > nums[x - 1]:
                nums[count] = nums[x]
                count += 1
        nums = nums[:count]
        return len(nums)

sol = Solution()
print(sol.removeDuplicates([2,5,5,11]))
