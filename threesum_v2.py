class Solution():
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        lst = set()
        for i in range(length):
            j = i + 1
            k = length - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    lst.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        return list(lst)

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
