class Solution():
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        lst = []
        for a in range(len(nums) - 3):
            for b in range(a + 1, len(nums) - 2):
                c = b + 1
                d = len(nums) - 1
                while c < d:
                    sum = nums[a] + nums[b] + nums[c] + nums[d]
                    print(a, b, c, d, sum, lst)
                    if sum < target:
                        c += 1
                    elif sum > target:
                        d -= 1
                    else:
                        ans = [nums[a], nums[b], nums[c], nums[d]]
                        if ans not in lst:
                            lst.append(ans)
                        d -= 1
        return lst

sol = Solution()
print(sol.fourSum([-3,-2,-1,0,0,1,2,3], 0))
