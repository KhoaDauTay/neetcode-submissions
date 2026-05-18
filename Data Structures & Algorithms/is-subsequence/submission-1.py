class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        # Khởi tạo bảng (m+1) x (n+1), mặc định False
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Base case: chuỗi rỗng là subsequence của mọi chuỗi
        for j in range(n + 1):
            dp[0][j] = True

        # Điền bảng
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # match → thu gọn cả 2
                else:
                    dp[i][j] = dp[i][j - 1]       # không match → bỏ t[j-1]

        return dp[m][n]
        