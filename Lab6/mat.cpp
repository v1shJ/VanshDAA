#include <iostream>
#include <vector>
#include <limits>
#include <stdexcept>
#include <string>
using namespace std;

// Base class for matrix chain calculations
class MatrixChainBase {
protected:
    vector<pair<int, int>> dimensions_;
    int n_;

    MatrixChainBase(const vector<pair<int, int>>& dimensions)
        : dimensions_(dimensions), n_(dimensions.size()) {
        if (n_ == 0) throw runtime_error("No matrices available.");
    }

    void validateDimensions() const {
        for (size_t i = 0; i < dimensions_.size() - 1; ++i) {
            if (dimensions_[i].second != dimensions_[i + 1].first) {
                throw runtime_error("Matrix dimensions are not conformable.");
            }
            if (dimensions_[i].first == 0 || dimensions_[i].second == 0) {
                throw runtime_error("Zero dimensions are not allowed.");
            }
        }
    }

    void printMatrixSequence(int i, int j) const {
        if (i == j) {
            cout << "C" << i + 1;
            return;
        }
        cout << "(";
        for (int k = i; k < j; ++k) {
            printMatrixSequence(i, k);
            cout << " x ";
            printMatrixSequence(k + 1, j);
        }
        cout << ")";
    }
};

// Optimized matrix chain multiplication with memoization
class MatrixChain : public MatrixChainBase {
private:
    vector<vector<int>> memo_;
    vector<vector<int>> sequence_;

    int calculateCost(int i, int j) {
        if (i == j) return 0;
        if (memo_[i][j] != -1) return memo_[i][j];

        int minCost = numeric_limits<int>::max();
        for (int k = i; k < j; ++k) {
            int cost = calculateCost(i, k) + calculateCost(k + 1, j) +
                      dimensions_[i].first * dimensions_[k].second * dimensions_[j].second;
            if (cost < minCost) {
                minCost = cost;
                sequence_[i][j] = k;
            }
        }
        memo_[i][j] = minCost;
        return minCost;
    }

    void printOptimalSequence(int i, int j) const {
        if (i == j) {
            cout << "C" << i + 1;
            return;
        }
        cout << "(";
        printOptimalSequence(i, sequence_[i][j]);
        printOptimalSequence(sequence_[i][j] + 1, j);
        cout << ")";
    }

public:
    MatrixChain(const vector<pair<int, int>>& dimensions) 
        : MatrixChainBase(dimensions) {
        memo_ = vector<vector<int>>(n_, vector<int>(n_, -1));
        sequence_ = vector<vector<int>>(n_, vector<int>(n_, -1));
    }

    void displayResults() {
        try {
            validateDimensions();
            cout << "Original multiplication sequence cost: " << bruteForceMinCost() << endl;
            cout << "Optimal multiplication sequence cost: " << findOptimalCost() << endl;
            cout << "Original multiplication sequence: ";
            printMatrixSequence(0, n_ - 1);
            cout << "\nOptimal multiplication sequence: ";
            printOptimalSequence(0, n_ - 1);
            cout << endl << endl;
        }
        catch (const exception& e) {
            cout << e.what() << endl;
        }
    }

    int findOptimalCost() {
        return calculateCost(0, n_ - 1);
    }

    int bruteForceMinCost() const {
        int totalCost = 0;
        for (size_t i = 0; i < dimensions_.size() - 1; ++i) {
            totalCost += dimensions_[i].first * dimensions_[i].second * dimensions_[i + 1].second;
        }
        return totalCost;
    }
};

// Brute force implementation
class MatrixChainBruteForce : public MatrixChainBase {
private:
    int bruteForceCost(int i, int j) {
        if (i == j) return 0;
        int minCost = numeric_limits<int>::max();
        for (int k = i; k < j; ++k) {
            int cost = bruteForceCost(i, k) + bruteForceCost(k + 1, j) + 
                      dimensions_[i].first * dimensions_[k].second * dimensions_[j].second;
            minCost = min(minCost, cost);
        }
        return minCost;
    }

public:
    MatrixChainBruteForce(const vector<pair<int, int>>& dimensions) 
        : MatrixChainBase(dimensions) {}

    void displayResults() {
        try {
            validateDimensions();
            cout << "Brute force minimum cost: " << bruteForceMinCost() << endl;
            cout << "Multiplication sequence: ";
            printMatrixSequence(0, n_ - 1);
            cout << endl;
        }
        catch (const exception& e) {
            cout << e.what() << endl;
        }
    }

    int bruteForceMinCost() {
        return bruteForceCost(0, n_ - 1);
    }
};

// Unified test class for both implementations
class MatrixChainTester {
private:
    void runSingleTest(const vector<pair<int, int>>& dimensions, const string& testName) {
        cout << "\nRunning " << testName << endl;
        try {
            MatrixChain optimal(dimensions);
            MatrixChainBruteForce bruteForce(dimensions);
            
            optimal.displayResults();
            bruteForce.displayResults();
        }
        catch (const runtime_error& e) {
            cout << "Test error: " << e.what() << endl;
        }
    }

public:
    void runAllTests() {
        // Positive test cases
        cout << "Running Positive Test Cases:\n";
        vector<vector<pair<int, int>>> positiveTests = {
            {{6, 7}, {7, 5}, {5, 4}},
            {{6, 8}, {8, 5}, {5, 4}, {4, 6}},
            {{6, 8}, {8, 5}, {5, 4}, {4, 6}, {6, 3}},
            {{6, 8}, {8, 5}, {5, 4}, {4, 6}, {6, 3}, {3, 5}},
            {{6, 8}, {8, 5}, {5, 4}, {4, 6}, {6, 3}, {3, 5}, {5, 7}, {7, 2}}
        };

        for (size_t i = 0; i < positiveTests.size(); ++i) {
            runSingleTest(positiveTests[i], "Positive Test Case " + to_string(i + 1));
        }

        // Negative test cases
        cout << "\nRunning Negative Test Cases:\n";
        vector<vector<pair<int, int>>> negativeTests = {
            {}, // Empty
            {{6, 7}, {5, 4}}, // Non-conformable
            {{6, 7}, {7, 0}, {0, 4}}, // Zero dimensions
            {{4, 4}, {4, 4}, {4, 4}} // Square matrices
        };

        for (size_t i = 0; i < negativeTests.size(); ++i) {
            runSingleTest(negativeTests[i], "Negative Test Case " + to_string(i + 1));
        }
    }
};

int main() {
    vector<pair<int, int>> testDimensions = {{6, 7}, {7, 5}, {5, 4}};
    MatrixChainTester tester;
    tester.runAllTests();
    return 0;
}