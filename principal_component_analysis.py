import numpy as np
import matplotlib.pyplot as plt


COLORS = [
    "tab:blue",
    "tab:orange",
    "tab:green",
    "tab:red",
]


def subplot(data, max_lim, x_plots, y_plots, plot_i, ground_truth):
    plt.subplot(y_plots, x_plots, plot_i)
    for i in range(len(data["data_1"])):
        plt.scatter(data["data_1"][i], data["data_2"][i], c=COLORS[ground_truth[i]])
    plt.xlabel(data["x_label"])
    plt.ylabel(data["y_label"])
    plt.xlim((0, max_lim))
    plt.ylim((0, max_lim))
    plt.xticks([0, max_lim])
    plt.yticks([0, max_lim])


def calculate_class(sample):
    x_class = np.array([0.00713349, 0.00706428, -0.00713349, 0.36180077])
    y_class = np.array([-0.14589178, 0.0015533, 0.14589178, -0.00713349])
    x = np.sum(x_class * sample)
    y = np.sum(y_class * sample)
    sample_class = 0
    if x < 1.5 and y < 0:
        sample_class = 0
    elif x > 1.5 and y < 0:
        sample_class = 1
    elif x < 1.5 and y > 0:
        sample_class = 2
    elif x > 1.5 and y > 0:
        sample_class = 3
    return sample_class


def main():
    # Data
    random_seed = 100
    np.random.seed(random_seed)
    samples = 100
    data = np.array([
        4.0 * np.random.uniform(0, 1, (samples)),
        1.0 * np.random.uniform(0, 1, (samples)),
        1.0 * np.random.uniform(0, 1, (samples)),
        8.0 * np.random.uniform(0, 1, (samples)),
    ])
    data[2] = -2.0 * (data[0] - data[0].max())
    ground_truth = []
    for i in range(samples):
        sample = data[:, i]
        ground_truth.append(calculate_class(sample))

    # Plot data with all 2 features
    covariance_matrix = np.cov(data)
    covariance_matrix /= np.sum(np.abs(covariance_matrix))
    for i in range(len(data)):
        for j in range(len(data)):
            datas = {
                "data_1": data[i],
                "data_2": data[j],
                "x_label": f"feature_{i+1}",
                "y_label": f"feature_{j+1}",
            }
            subplot(datas, 8, len(data), len(data), 1+i*len(data)+j, ground_truth)
    plt.suptitle("Variance in 2 dimensions")
    plt.tight_layout()
    plt.show()

    # Plot covariance matrix
    plt.matshow(covariance_matrix)
    plt.title("Covariance matrix")
    plt.colorbar()
    for (i, j), z in np.ndenumerate(covariance_matrix):
        plt.text(j, i, "{:0.2f}".format(z), ha="center", va="center",
            bbox=dict(boxstyle="round", facecolor="white", edgecolor="0.3"))
    plt.show()

    # Print components
    print("Principal components with highest value")
    for i in range(covariance_matrix.shape[0]):
        print(f"PC {i+1}:", np.sum(np.abs(covariance_matrix[i])))

    # Select 2 best eigen vectors
    highest_score_pc = np.argsort(np.abs(covariance_matrix).sum(axis=1))
    eigen_vector_x = covariance_matrix[highest_score_pc[-1]]
    eigen_vector_y = covariance_matrix[highest_score_pc[-2]]

    # Calculate PC samples
    pc_x_data = []
    pc_y_data = []
    for i in range(samples):
        sample_features = data[:, i]
        pc_x_data.append(np.sum(eigen_vector_x * sample_features))
        pc_y_data.append(np.sum(eigen_vector_y * sample_features))

    # Plot PC data
    for i in range(samples):
        plt.scatter(pc_x_data[i], pc_y_data[i], c=COLORS[ground_truth[i]])
    plt.title("Principal component analysis (PCA)")
    plt.xlabel(f"PC{highest_score_pc[-1]}")
    plt.ylabel(f"PC{highest_score_pc[-2]}")
    plt.show()


main()
