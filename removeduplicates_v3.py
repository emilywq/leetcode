class Solution():
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxVolume = 0
        i = 0
        j = len(height) - 1
        while i < j:
            volume = min(height[i], height[j]) * (j - i)
            maxVolume = max(volume, maxVolume)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxVolume

sol = Solution()
print(sol.removeDuplicates([2,5,5,11]))
