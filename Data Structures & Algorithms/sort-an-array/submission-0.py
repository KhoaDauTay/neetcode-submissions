class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        MERGE_SORT(arr):
            if len(arr) <= 1:
                return arr

            mid   = len(arr) // 2
            left  = MERGE_SORT(arr[:mid])
            right = MERGE_SORT(arr[mid:])

            return MERGE(left, right)


        MERGE(left, right):
            result = []
            i = 0, j = 0

            while i < len(left) AND j < len(right):
                if left[i] <= right[j]:
                    append left[i] to result
                    i++
                else:
                    append right[j] to result
                    j++

            append remaining left[i:] to result
            append remaining right[j:] to result

            return result
        """
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)
        
    def merge(self, left, right):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result