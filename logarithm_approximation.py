import math
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

INITIAL_GUESS = [
    0.5,
    1.5,
    2.5,
    3.5,
    4.5,
    5.5,
    6.5,
    7.5,
    8.5,
    9.5,
    10.5,
    11.5,
    12.5,
    13.5,
    14.5,
    15.5,
    16.5,
    17.5,
    18.5,
    19.5,
    20.5,
    21.5,
    22.5,
    23.5,
    24.5,
    25.5,
    26.5,
    27.5,
    28.5,
    29.5,
    30.5,
    31.5,
]
INPUT_VALUE = [
    2**1,
    2**2,
    2**3,
    2**4,
    2**5,
    2**6,
    2**7,
    2**8,
    2**9,
    2**10,
    2**11,
    2**12,
    2**13,
    2**14,
    2**15,
    2**16,
    2**17,
    2**18,
    2**19,
    2**20,
    2**21,
    2**22,
    2**23,
    2**24,
    2**25,
    2**26,
    2**27,
    2**28,
    2**29,
    2**30,
    2**31,
    2**32,
]


def searchSegment(x):
    # 5 flops: range(1, 2**32)
    # ceil(log2(len(lut)))
    # No extra flops with manual binary search

    if x < INPUT_VALUE[15]:
        if x < INPUT_VALUE[7]:
            if x < INPUT_VALUE[3]:
                if x < INPUT_VALUE[1]:
                    if x < INPUT_VALUE[0]:
                        i = 0
                    else:
                        i = 1
                else:
                    if x < INPUT_VALUE[2]:
                        i = 2
                    else:
                        i = 3
            else:
                if x < INPUT_VALUE[5]:
                    if x < INPUT_VALUE[4]:
                        i = 4
                    else:
                        i = 5
                else:
                    if x < INPUT_VALUE[6]:
                        i = 6
                    else:
                        i = 7
        else:
            if x < INPUT_VALUE[11]:
                if x < INPUT_VALUE[9]:
                    if x < INPUT_VALUE[8]:
                        i = 8
                    else:
                        i = 9
                else:
                    if x < INPUT_VALUE[10]:
                        i = 10
                    else:
                        i = 11
            else:
                if x < INPUT_VALUE[13]:
                    if x < INPUT_VALUE[12]:
                        i = 12
                    else:
                        i = 13
                else:
                    if x < INPUT_VALUE[14]:
                        i = 14
                    else:
                        i = 15
    else:
        if x < INPUT_VALUE[23]:
            if x < INPUT_VALUE[19]:
                if x < INPUT_VALUE[17]:
                    if x < INPUT_VALUE[16]:
                        i = 16
                    else:
                        i = 17
                else:
                    if x < INPUT_VALUE[18]:
                        i = 18
                    else:
                        i = 19
            else:
                if x < INPUT_VALUE[21]:
                    if x < INPUT_VALUE[20]:
                        i = 20
                    else:
                        i = 21
                else:
                    if x < INPUT_VALUE[22]:
                        i = 22
                    else:
                        i = 23
        else:
            if x < INPUT_VALUE[27]:
                if x < INPUT_VALUE[25]:
                    if x < INPUT_VALUE[24]:
                        i = 24
                    else:
                        i = 25
                else:
                    if x < INPUT_VALUE[26]:
                        i = 26
                    else:
                        i = 27
            else:
                if x < INPUT_VALUE[29]:
                    if x < INPUT_VALUE[28]:
                        i = 28
                    else:
                        i = 29
                else:
                    if x < INPUT_VALUE[31]:
                        i = 31
                    else:
                        i = 32
    return i


def log2(x):
    i = searchSegment(x)
    y1 = INITIAL_GUESS[i]
    y2 = INITIAL_GUESS[i+1]
    x1 = INPUT_VALUE[i]
    x2 = INPUT_VALUE[i+1]
    dx = x2 - x1  # Constant, can be done with LUT
    dy = 1  # y2 - y1, constant
    a = dy / dx  # Constant

    # 3 flops to interpolate
    return a * (x - x1) + y1


def main():
    input_values = list(range(1, 2**26, 1))

    # Calculate logarithms
    errors = []
    threshold = 1
    threshold_count = 0
    progress_bar = tqdm(input_values)
    approximated_values = []
    real_values = []
    for input_value in progress_bar:
        result = log2(input_value)
        real_log2 = math.log(input_value, 2)
        relative_error = round(abs(real_log2 - result) / (1e-5 + math.log(input_value, 2)) * 100, 2)
        if relative_error > 1:
            threshold_count += 1
        errors.append(relative_error)
        approximated_values.append(result)
        real_values.append(real_log2)
    print(f">{threshold}%: {round(100 * threshold_count / len(progress_bar), 2)}%")
    print(f"Max error: {max(errors)}%")
    print(f"Average error: {round(np.mean(np.array(errors)), 6)}%")

    # Plot
    #plt.plot(list(range(len(errors))), len(errors) * [threshold], color="tab:gray", alpha=0.5)
    total_flops = 8

    # Linear
    plt.plot(input_values, errors)
    plt.title(f"Log2 approximation with {total_flops} FLOPS")
    plt.xlabel("x")
    plt.ylabel("Relative error (%)")
    plt.savefig(f"log2_{total_flops}-flops_linear.png")

    # Logarithmic
    plt.xscale("log")
    plt.title(f"Log2 approximation with {total_flops} FLOPS")
    plt.xlabel("x")
    plt.ylabel("Relative error (%)")
    plt.savefig(f"log2_{total_flops}-flops_logarithmic.png")
    plt.close()

    # Overlay results
    plt.plot(input_values, real_values, label="Real")
    plt.plot(input_values, approximated_values, label="Approximated")
    plt.legend()
    plt.xscale("log")
    plt.title(f"Log2 approximation with {total_flops} FLOPS")
    plt.xlabel("x")
    plt.ylabel("log2(x)")
    plt.savefig(f"log2_{total_flops}-flops_logarithmic_comparison.png")


main()
