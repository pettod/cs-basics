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
    threshold = 1
    threshold_count = 0
    progress_bar = tqdm(input_values)
    for input_value in progress_bar:
        result = log2(input_value, iterations)
        relative_error = round(abs(input_value - result ** 2) / input_value * 100, 2)
        if relative_error > 1:
            threshold_count += 1
        #progress_bar.set_description(f">{threshold}%: {threshold_count}")  # This is SLOW!
        errors.append(relative_error)
    print(f">{threshold}%: {round(100 * threshold_count / len(progress_bar), 2)}%")
    print(f"Max error: {max(errors)}%")
    print(f"Average error: {round(np.mean(np.array(errors)), 6)}%")

    # Plot
    #plt.plot(list(range(len(errors))), len(errors) * [threshold], color="tab:gray", alpha=0.5)
    plt.plot(errors)
    lut_ops = math.ceil(math.log2(len(LUT_VALUE))) + 1
    total_ops = iterations * 3 + lut_ops
    plt.title(f"log2() approximation with {total_ops} OPS")
    plt.xlabel("Input digit")
    plt.ylabel("Relative error (%)")
    plt.savefig(f"newton-raphson_logarithm_{total_ops}-ops.png")


main()
