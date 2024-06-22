class Solution():
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        dict = {}
        lst = []
        for i, v in enumerate(nums):
            dict[v] = i
        for a in range(len(nums) - 3):
            for b in range(a + 1, len(nums) - 2):
                for c in range(b + 1, len(nums) - 1):
                    sum = nums[a] + nums[b] + nums[c]
                    complement = target - sum
                    value = dict.get(complement)
                    if value is not None and a != value and b != value and c != value:
                        ans = [nums[a], nums[b], nums[c], complement]
                        ans.sort()
                        if ans not in lst:
                            lst.append(ans)
        return lst

sol = Solution()
print(sol.fourSum([-3,-2,-1,0,0,1,2,3], 0))
