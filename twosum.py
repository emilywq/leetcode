class Solution():
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i, v in enumerate(nums):
            dict[v] = i
        for x in range(len(nums)):
            find = target - nums[x]
            value = dict.get(find)
            if value is not None:
                if x != value:
                    return [x, value]

sol = Solution()
print(sol.twoSum([2,5,5,11], 10))
