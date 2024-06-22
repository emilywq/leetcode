class Solution():
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closestsum = None
        mindifference = None
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    sum = nums[i] + nums[j] + nums[k]
                    difference =  abs(sum - target)
                    if mindifference is None or difference < mindifference:
                        mindifference = difference
                        closestsum = sum
        return closestsum

sol = Solution()
print(sol.threeSumClosest([1,1,1,0], -100))
