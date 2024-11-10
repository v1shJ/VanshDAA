import random

def longest_common_subsequence(seq1, seq2):
    n, m = len(seq1), len(seq2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtracking to find the LCS sequence
    i, j = n, m
    lcs = []
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs.append(seq1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs[::-1]  # Reverse the list to get the correct order


def generate_random_grades(n = 20, ming = 5, maxg = 10):
    
    grades = ["AA", "AB", "BB", "BC", "CC", "CD", "DD", "FF"]
    res = []
    for i in range(n):
        seq1 = seq2 = []
        for _ in range(random.randint(1, 10)):
            seq1.append(grades[random.randint(1, 7)])
            seq2.append(grades[random.randint(1, 7)])
        print(f"StudentA {i+1}: {seq1} \nStudentB {i+1}: {seq2}")
        ans = longest_common_subsequence(seq1, seq2)
        print(f"Their Longest Common Subsequence: {ans}")
        res.append(ans)
        print("\n\n")

generate_random_grades()