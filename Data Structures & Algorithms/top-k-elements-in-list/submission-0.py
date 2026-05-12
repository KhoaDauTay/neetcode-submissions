class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Bước 1: đếm tần suất
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # Bước 2: tạo bucket, index = tần suất
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            bucket[count].append(num)

        # Bước 3: quét từ cuối, nhặt đủ k phần tử
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
        