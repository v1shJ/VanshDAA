import math
import time
from random import randint

class BigIntegerMultiplier:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Integer Multiplication Without DAC
    @staticmethod
    def intmult(a, b):
        a, b = min(a, b), max(a, b)
        prod = 0
        n = i = len(str(a))
        while a > 0:
            i -= 1
            prod += a % 10 * b * (10 ** (n - i - 1))
            a //= 10
        return prod

    def get_min_length(self, n1, n2):
        n1_length = 0
        n2_length = 0
        if n1 == 0: n1_length = 1
        else: n1_length = math.floor(math.log10(n1)) + 1
        
        if n2 == 0: n2_length = 1
        else: n2_length = math.floor(math.log10(n2)) + 1

        return min(n1_length, n2_length)

    def karatsuba(self):
        x, y = self.x, self.y
        sign = 1
        if x < 0 or y < 0:
            sign = -1
        x = abs(x)
        y = abs(y)

        if x < 10 or y < 10:
            return sign * (x * y)
        
        m = self.get_min_length(x, y)
        m2 = m // 2
        
        high1, low1 = divmod(x, 10 ** m2)         # Equivalent to splitting in the middle
        high2, low2 = divmod(y, 10 ** m2)
        
        z0 = self.karatsuba_helper(low1, low2)
        z2 = self.karatsuba_helper(high1, high2)
        z1 = self.karatsuba_helper(low1 + high1, low2 + high2) - z2 - z0
        # outputs low1low2 + low1high2 + high1low2 + high1high2
        # from which we must subtract low1low2(z0) and high1high2(z2)
        
        return sign * (z2 * (10 ** (m2 * 2)) + z1 * (10 ** m2) + z0)

    @staticmethod
    def karatsuba_helper(a, b):
        multiplier = BigIntegerMultiplier(a, b)
        return multiplier.karatsuba()

    def measure_times(self):
        # Measure Karatsuba timing
        start_time = time.time()
        karatsuba_result = self.karatsuba()
        karatsuba_time = (time.time() - start_time) * 1000

        # Measure built-in operator timing
        start_time = time.time()
        normal_result = self.x * self.y 
        normal_time = (time.time() - start_time) * 1000

        try:
            assert karatsuba_result == normal_result
            # Output results
            print(f"x: {self.x} \n\n y: {self.y} \n\n")
            print(f"Karatsuba result: {karatsuba_result}")
            print(f"Karatsuba time: {karatsuba_time:.6f} milliseconds")
            print(f"Normal multiplication result: {normal_result}")
            print(f"Normal multiplication time: {normal_time:.6f} milliseconds")
        except AssertionError:
            print("Results do not match!")

# Generate random large integers of 1000 length
x = randint(10**999, 10**1000)
y = randint(10**999, 10**1000)

testcases = (
    (1000000000, 9000000000),
    (0, 91934144948149581359),
    (-135, 85319),
    (91333333333333, 83059139037509173),
    (0, 0),
    (randint(10**999, 10**1000), randint(10**999, 10**1000)),
    (randint(10**499, 10**500), randint(10**499, 10**500)),
    (randint(10**99, 10**100), randint(10**99, 10**100)),
    (randint(10**49, 10**50), randint(10**49, 10**50)),
    ("hello", "world")
)

multiplier = BigIntegerMultiplier(x, y)
multiplier.measure_times()

for x, y in testcases:
    print("\n\n\n\n")
    if type(x) == int and type(y) == int:    
        multiplier = BigIntegerMultiplier(x, y)
        multiplier.measure_times()
    else:
        print(f"GIVEN INPUTS x: {x} y: {y} \nThey're {type(x)}. CONVERT TO INTEGERS")
