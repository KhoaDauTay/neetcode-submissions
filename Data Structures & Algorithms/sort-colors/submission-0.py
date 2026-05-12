class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        low=0, mid=0, high=3
        red: low, mid-1, white: mid, high -1, blue: high ++
        """
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                self.swap(nums, low, mid)
                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                self.swap(nums, mid, high)
                high -= 1

        return nums
            
    def swap(self, nums, l, r):
        tmp = nums[l]
        nums[l] = nums[r]
        nums[r] = tmp

        