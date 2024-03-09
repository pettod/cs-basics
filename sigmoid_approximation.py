import math
import matplotlib.pyplot as plt
import numpy as np


def sigmoid(x):
    # 4 flops
    c = 0.36787944117144233
    if x >= 0:
        return 1 - c / (1 + x)
    else:
        return c / (1 - x)


def main():
    real = []
    approximated = []
    data_range = np.arange(-20, 20, 0.1)
    for input_value in data_range:
        approximated_ = sigmoid(input_value)
        real_ = 1 / (1 + math.exp(-input_value))
        real.append(real_)
        approximated.append(approximated_)

    # Plot
    plt.plot(data_range, real, label="Real")
    plt.plot(data_range, approximated, label="Approximated")
    plt.legend()
    plt.title("Sigmoid approximation with 4 FLOPS")
    plt.savefig("sigmoid.png")


main()
