# Some basic CS and ML algos

## Monte Carlo

Estimating $\pi$ with Monte Carlo technique.

The area of a circle is:

$A_{circle} = \pi r^{2}$

And the area of a square is:

$A_{square} = (2 * r) ^ 2 = 4 r^{2}$

A uniform random sampling is applied to the area of the square and the number of the points which hit the area of the circle are calculated. To estimate $\pi$, a relation is calculated between the number of points in the circle and in the whole square.

$\frac{A_{circle}}{A_{square}} = \frac{N_{circle}}{N_{square}} = \frac{\pi r^{2}}{4 r^{2}}$

Now, by simplifying the formula, $\pi$ is estimated:

$\pi = 4 \frac{N_{circle}}{N_{square}}$

![pi_monte_carlo](https://github.com/pettod/merge-sort/assets/33998401/2dfb94b0-c2f5-4eae-8fa8-46456341ec8d)

## Principal component analysis (PCA)

Reducing dimensions by computing eigen vectors and selecting the ones with the highest variance. With the new principal components it is easier to visualize the data.

![pca_1](https://github.com/pettod/cs-basics/assets/33998401/14509b40-50d6-4165-b3d3-0b153114dec4)
![pca_2](https://github.com/pettod/cs-basics/assets/33998401/3b5169b6-c4d7-4683-af4e-742c68063a22)
![pca_3](https://github.com/pettod/cs-basics/assets/33998401/86c0f9fc-44fc-4224-8d98-8b747c9b6b64)


## Merge sort

Recursive merge sort. Graphs show the time complexity.

![measurements](https://github.com/pettod/merge-sort/assets/33998401/26d45a62-c7aa-4397-be0e-de050021b0ee)
