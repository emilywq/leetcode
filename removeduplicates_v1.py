class Solution():
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniquenums = []
        count = 0
        for x in range(len(nums)):
            if nums[x] not in uniquenums:
                uniquenums.append(nums[x])
                nums[count] = nums[x]
                count += 1
        print(nums)
        return len(uniquenums)

sol = Solution()
print(sol.removeDuplicates([2,5,5,11]))
