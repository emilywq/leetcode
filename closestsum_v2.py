class Solution():
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        print(nums)
        closestsum = None
        mindifference = None
        for i in range(len(nums) - 1):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                difference =  abs(sum - target)
                print(i, j, k, sum, difference)
                if mindifference is None or difference < mindifference:
                    mindifference = difference
                    closestsum = sum
                if sum > target:
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    break
        return closestsum

sol = Solution()
print(sol.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))
