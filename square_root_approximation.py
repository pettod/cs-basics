import math
import matplotlib.pyplot as plt
import numpy as np
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


def squareRoot(x, iterations=10):
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
    threshold = 1
    threshold_count = 0
    progress_bar = tqdm(input_values)
    approximated_values = []
    real_values = []
    for input_value in progress_bar:
        result = squareRoot(input_value, iterations)
        real_sqrt = math.sqrt(input_value)
        relative_error = round(abs(real_sqrt - result) / real_sqrt * 100, 2)
        if relative_error > 1:
            threshold_count += 1
        errors.append(relative_error)
        approximated_values.append(result)
        real_values.append(real_sqrt)
    print(f">{threshold}%: {round(100 * threshold_count / len(progress_bar), 2)}%")
    print(f"Max error: {max(errors)}%")
    print(f"Average error: {round(np.mean(np.array(errors)), 6)}%")

    # Plot
    lut_ops = math.ceil(math.log2(len(LUT_VALUE))) + 1
    total_ops = 3 * iterations + lut_ops

    # Linear
    plt.plot(input_values, errors)
    plt.title(f"Square root approximation with {total_ops} OPS")
    plt.xlabel("Digit")
    plt.ylabel("Relative error (%)")
    plt.savefig(f"square-root_{total_ops}-ops_linear.png")

    # Logarithmic
    plt.xscale("log")
    plt.title(f"Square root approximation with {total_ops} OPS")
    plt.xlabel("Digit")
    plt.ylabel("Relative error (%)")
    plt.savefig(f"square-root_{total_ops}-ops_logarithmic.png")
    plt.close()

    # Overlay results
    plt.plot(input_values, approximated_values, label="Approximated")
    plt.plot(input_values, real_values, label="Real")
    plt.xscale("log")
    plt.yscale("log")
    plt.title(f"Square root approximation with {total_ops} OPS")
    plt.xlabel("x")
    plt.ylabel("sqrt(x)")
    plt.savefig(f"square-root_{total_ops}-ops_logarithmic_comparison.png")


main()
