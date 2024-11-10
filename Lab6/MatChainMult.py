import sys

# Base class for matrix chain calculations
class MatrixChainBase:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.n = len(dimensions)
        if self.n == 0:
            raise RuntimeError("No matrices available.")

    def validate_dimensions(self):
        for i in range(self.n - 1):
            if self.dimensions[i][1] != self.dimensions[i + 1][0]:
                raise RuntimeError(f"Matrix {i + 1} and Matrix {i + 2} are not conformable.")
            if self.dimensions[i][0] == 0 or self.dimensions[i][1] == 0:
                raise RuntimeError(f"Matrix {i + 1} has zero dimensions.")

    def print_matrix_sequence(self, i, j):
        if i == j:
            print(f"M{i + 1}", end="")
            return
        print("(", end="")
        for k in range(i, j):
            self.print_matrix_sequence(i, k)
            print(" x ", end="")
            self.print_matrix_sequence(k + 1, j)
        print(")", end="")

# Optimized matrix chain multiplication with dynamic programming
class MatrixChain(MatrixChainBase):
    def __init__(self, dimensions):
        super().__init__(dimensions)
        self.memo = [[-1] * self.n for _ in range(self.n)]
        self.sequence = [[-1] * self.n for _ in range(self.n)]

    def calculate_cost(self, i, j):
        if i == j:
            return 0
        if self.memo[i][j] != -1:
            return self.memo[i][j]

        min_cost = sys.maxsize
        for k in range(i, j):
            cost = (self.calculate_cost(i, k) + 
                    self.calculate_cost(k + 1, j) + 
                    self.dimensions[i][0] * self.dimensions[k][1] * self.dimensions[j][1])
            if cost < min_cost:
                min_cost = cost
                self.sequence[i][j] = k

        self.memo[i][j] = min_cost
        return min_cost

    def print_optimal_sequence(self, i, j):
        if i == j:
            print(f"M{i + 1}", end="")
            return
        print("(", end="")
        self.print_optimal_sequence(i, self.sequence[i][j])
        print(" x ", end="")
        self.print_optimal_sequence(self.sequence[i][j] + 1, j)
        print(")", end="")

    def display_results(self):
        if self.n == 1:
            print("Only one matrix, no multiplication required.")
            return
        try:
            self.validate_dimensions()
            print(f"Optimal multiplication sequence cost: {self.find_optimal_cost()}")
            print("Optimal multiplication sequence: ", end="")
            self.print_optimal_sequence(0, self.n - 1)
            print("\n")
        except Exception as e:
            print(f"Error: {e}")

    def find_optimal_cost(self):
        return self.calculate_cost(0, self.n - 1)

# Unified test class for the DP implementation
class MatrixChainTester:
    def run_single_test(self, dimensions, test_name):
        print(f"\nRunning {test_name}")
        try:
            optimal = MatrixChain(dimensions)
            optimal.display_results()
        except RuntimeError as e:
            print(f"Test error: {e}")

    def run_all_tests(self):
        # Positive test cases
        print("Running Positive Test Cases:")
        positive_tests = [
            [(6, 7), (7, 5), (5, 4)],
            [(6, 8), (8, 5), (5, 4), (4, 6)],
            [(6, 8), (8, 5), (5, 4), (4, 6), (6, 3)],
            [(6, 8), (8, 5), (5, 4), (4, 6), (6, 3), (3, 5)],
            [(6, 8), (8, 5), (5, 4), (4, 6), (6, 3), (3, 5), (5, 7), (7, 2)]
        ]

        for idx, test in enumerate(positive_tests):
            self.run_single_test(test, f"Positive Test Case {idx + 1}")

        # Negative test cases
        print("\nRunning Negative Test Cases:")
        negative_tests = [
            [],  # Empty
            [(6, 7), (5, 4)],  # Non-conformable
            [(6, 7), (7, 0), (0, 4)],  # Zero dimensions
            [(4, 4), (4, 4), (4, 4)]  # Square matrices
        ]

        for idx, test in enumerate(negative_tests):
            self.run_single_test(test, f"Negative Test Case {idx + 1}")

if __name__ == "__main__":
    tester = MatrixChainTester()
    tester.run_all_tests()
