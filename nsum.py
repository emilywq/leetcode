class Solution():
    def nSum(self, nums, n, target):
        """
        :type nums: List[int]
        :type n: int
        # n is the required number of integers used to sum up to the given target
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        lst = set()

        if n == 2:
            x = 0
            y = length - 1
            while x < y:
                sum = nums[x] + nums[y]
                if sum < target:
                    x += 1
                elif sum > target:
                    y -= 1
                else:
                    lst.add((nums[x], nums[y]))
                    y -= 1
            return lst

        else:
            for i in range(length):
                ret = self.nSum(nums[i+1:], n-1, target-nums[i])
                for v in ret:
                    lst.add(tuple([nums[i]] + list(v)))
            return [list(tup) for tup in lst]

sol = Solution()
print(sol.nSum([-1,0,1,2,-1,-4], 4, 0))
