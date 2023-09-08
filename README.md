# Some basic CS and ML algos

Collection of multiple basic concepts in computer science and machine learning.

## Monte Carlo

Estimating $\pi$ with Monte Carlo technique.

The area of a circle is:

$$
A_{circle} = \pi r^{2}
$$

And the area of a square is $a ^ 2$ where $a = 2 r$:

$$
A_{square} = (2r) ^ 2 = 4 r^{2}
$$

A uniform random sampling is applied to the area of the square and the number of the points which hit the area of the circle are calculated. To estimate $\pi$, a relation is calculated between the number of points in the circle and in the whole square.

$$
\frac{A_{circle}}{A_{square}} = \frac{N_{circle}}{N_{square}} = \frac{\pi r^{2}}{4 r^{2}}
$$

Now, by simplifying the formula, $\pi$ is estimated:

$$
\pi = 4 \frac{N_{circle}}{N_{square}}
$$

![pi_monte_carlo](https://github.com/pettod/merge-sort/assets/33998401/2dfb94b0-c2f5-4eae-8fa8-46456341ec8d)

## Principal component analysis (PCA)

Reducing 4 dimensional data to 2 by computing eigen vectors and selecting the ones with the highest variance. With the new principal components it is easier to visualize the data.

![pca](https://github.com/pettod/cs-basics/assets/33998401/2d84a9ba-a9a3-4cf8-b49b-fa072aaf9273)

## Merge sort

Recursive merge sort. Graphs show the time complexity.

![measurements](https://github.com/pettod/merge-sort/assets/33998401/26d45a62-c7aa-4397-be0e-de050021b0ee)
