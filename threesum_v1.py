class Solution():
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dict = {}
        for i, v in enumerate(nums):
            dict[v] = i
        length = len(nums)
        lst = []
        for i in range(length):
            for j in range(i + 1, length):
                needednum = -(nums[i] + nums[j])
                k = dict.get(needednum)
                if k is not None:
                    if k > j:
                        templst = [nums[i], nums[j], needednum]
                        templst.sort()
                        if templst not in lst:
                            lst.append(templst)
        return lst

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
