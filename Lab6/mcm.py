def matrix_chain_multiplication(N, arr):
    """
    Computes the optimal order of multiplying matrices to minimize the number of scalar multiplications.
    """
    if len(arr) < 2:
        return 0, "No matrices provided"
    if len(arr) == 2:
        return 0, "Only one matrix provided"
    if any(k < 0 for k in arr):
        return -1, "Matrix dimensions must be positive"

    dp = [[0 for _ in range(N)] for _ in range(N)]
    split = [[0 for _ in range(N)] for _ in range(N)]

    for L in range(2, N):
        for i in range(1, N - L + 1):
            j = i + L - 1
            dp[i][j] = float('inf')
            
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                if q < dp[i][j]:
                    dp[i][j] = q
                    split[i][j] = k

    def get_optimal_order(i, j):
        if i == j:
            return f"A{i}"
        k = split[i][j]
        left_order = get_optimal_order(i, k)
        right_order = get_optimal_order(k + 1, j)
        return f"({left_order} x {right_order})"

    optimal_order = get_optimal_order(1, N - 1)
    return dp[1][N - 1], optimal_order

def tests():
    """
    Finds the optimal order of multiplying matrices for different metereological matrix dimensions.
    """
    test_cases = [
        [7, 3, 7, 4, 7, 5, 7, 6],
        [7, 5, 7, 6, 7, 7, 7, 8],
        [7, 4, 7, 8, 7, 3, 7, 9],
        [7, 2, 7, 10, 7, 4, 7, 5],
        [7, 6, 7, 3, 7, 8, 7, 2],
        [7, 9, 7, 5, -7, 10, -7, 3],
        [7, 7],
        [7, -10, 7, 3, -7, 9, 7, 5],
        [10],
        []
    ]
    for tc in test_cases:
        print(matrix_chain_multiplication(len(tc), tc))
    
tests()