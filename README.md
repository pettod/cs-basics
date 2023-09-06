# Some basic CS and ML algos

## Merge sort

Recursive merge sort. Graphs show the time complexity.

![measurements](https://github.com/pettod/merge-sort/assets/33998401/26d45a62-c7aa-4397-be0e-de050021b0ee)

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
