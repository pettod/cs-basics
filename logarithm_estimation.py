import math
import matplotlib.pyplot as plt
from tqdm import tqdm


LUT_DIVIDER = [
    1.6,
    10.0,
    30.0,
    130.0,
    500.0,
    1000.0,
    2000.0,
    5000.0,
]
LUT_VALUE = [
    2**4,
    2**8,
    2**12,
    2**16,
    2**19,
    2**21,
    2**23,
]


def initialGuess(x, mid=None, left=None, right=None):
    # ceil(log2(len(lut_table))) + 1 ops

    # No extra ops with manual binary search
    if x < LUT_VALUE[3]:
        if x < LUT_VALUE[1]:
            if x < LUT_VALUE[0]:
                divider = LUT_DIVIDER[0]
            else:
                divider = LUT_DIVIDER[1]
        else:
            if x < LUT_VALUE[2]:
                divider = LUT_DIVIDER[2]
            else:
                divider = LUT_DIVIDER[3]
    else:
        if x < LUT_VALUE[5]:
            if x < LUT_VALUE[4]:
                divider = LUT_DIVIDER[4]
            else:
                divider = LUT_DIVIDER[5]
        else:
            if x < LUT_VALUE[6]:
                divider = LUT_DIVIDER[6]
            else:
                divider = LUT_DIVIDER[7]
    return x / divider


def log2(x, iterations=10):
    guess = initialGuess(x)

    # 3 ops per iteration
    # Newton-Raphson iteration
    # https://www.geeksforgeeks.org/newton-raphson-method/
    for _ in range(iterations):
        guess = (guess + x / guess) / 2.0
    return guess


def main():
    iterations = 3
    input_values = list(range(1, 2**26, 10))

    # Calculate logarithms
    errors = []
    for input_value in tqdm(input_values):
        result = log2(input_value, iterations)
        relative_error = round(abs(input_value - result ** 2) / input_value * 100, 2)
        if relative_error < 1:
            print(input_value)
        errors.append(relative_error)

    # Plot
    plt.plot(errors)
    lut_ops = math.ceil(math.log2(len(LUT_VALUE))) + 1
    total_ops = iterations * 3 + lut_ops
    plt.title(f"log2() estimation with {iterations} * 3 + {lut_ops} ops = {total_ops} ops")
    plt.xlabel("Input digit")
    plt.ylabel("Relative Error (%)")
    plt.savefig(f"newton-raphson_logarithm_{total_ops}-ops.png")


main()
