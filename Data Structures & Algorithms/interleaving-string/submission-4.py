class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        # stores if we can use s1[:i], and s2[:j] to form s3[:i + j]
        dp = [False] * (len(s2) + 1)
        dp[0] = True

        # s1 is not considered and we check all substrings of s2
        for j in range(1, len(s2) + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, len(s1) + 1):
            # check s1s match every time
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, len(s2) + 1):
                from_s1 = dp[j] and s1[i - 1] == s3[i + j - 1]
                from_s2 = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                # This prefix is valid if its last character can come from s1 or s2,
                # and the corresponding earlier prefix was already valid.
                dp[j] = from_s1 or from_s2

        return dp[len(s2)]