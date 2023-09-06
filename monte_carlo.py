import math
import matplotlib.pyplot as plt
import random
from tqdm import tqdm


def main():
    max_n = 2**21

    circle_x = []
    circle_y = []
    square_x = []
    square_y = []
    pi_estimations = []
    plot_n = []
    circle_count = 0
    square_count = 0
    radius = 1
    radius_squared = radius**2
    plot_index = 5
    for n in tqdm(range(1, 1+max_n)):
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)
        if (x**2 + y**2) < radius_squared:
            circle_count += 1
            circle_x.append(x)
            circle_y.append(y)
        else:
            square_count += 1
            square_x.append(x)
            square_y.append(y)

        if n == plot_index:
            plot_n.append(n)
            pi = 4*circle_count/n
            pi_estimations.append(pi)

            plt.figure(figsize=(10.5, 5))
            plt.subplot(1,2,1)
            plt.title("n = {:,.0f}".format(n))
            plt.scatter(circle_x, circle_y, s=1.0)
            plt.scatter(square_x, square_y, s=1.0)
            plt.xlim((-radius, radius))
            plt.ylim((-radius, radius))
            plt.xticks([])
            plt.yticks([])

            plt.subplot(1,2,2)
            plt.title("π = {:.6f}".format(pi))
            plt.plot(len(pi_estimations)*[math.pi], label="Real π")
            plt.plot(pi_estimations, label="Estimated π")
            plt.ylim((2, 4))
            plt.yticks([2,3,4])
            plt.xticks([])
            plt.legend()
            plt.savefig(f"frames/{n:07}.png")
            plt.close()
            plot_index = int(1.2 * plot_index)


main()
