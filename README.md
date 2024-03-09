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

A uniform random sampling is applied to the area of the square and the number of the points which hit the area of the circle are counted. To estimate $\pi$, the relationship between the number of points in the circle and in the whole square is calculated.

$$
\frac{A_{circle}}{A_{square}} = \frac{N_{circle}}{N_{square}} = \frac{\pi r^{2}}{4 r^{2}}
$$

Now, by simplifying the formula, $\pi$ is estimated:

$$
\pi = 4 \frac{N_{circle}}{N_{square}}
$$

![pi_monte_carlo](https://github.com/pettod/merge-sort/assets/33998401/2dfb94b0-c2f5-4eae-8fa8-46456341ec8d)

## Principal component analysis (PCA)

Reducing 4 dimensional data to 2 by computing eigenvectors and selecting the ones with the highest variance. With the new principal components it is easier to visualize the data.

![pca](https://github.com/pettod/cs-basics/assets/33998401/2d84a9ba-a9a3-4cf8-b49b-fa072aaf9273)

## Square root approximation and FLOPS

Approximating square root function with an integer range from 1 to 2<sup>26</sup> = 67,108,864 using [Newton-Raphson method](https://en.wikipedia.org/wiki/Newton%27s_method) and a small, memory efficient [lookup table](https://en.wikipedia.org/wiki/Lookup_table) (LUT).

In Newton-Raphson method, you start with an initial value $x_0$ and take iterative steps towards a more accurate approximation using the following formula

$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)},
$$

where $x_n$ is the initial value of $x$, $f(x_n)$ is the value of the equation at initial value, and $f'(x_n)$ is the value of the first order derivative of the equation or function at the initial value $x_n$. The figure below illustrates the iterative approach.

![newton_raphson_method](https://github.com/pettod/cs-basics/assets/33998401/457aec38-4cca-419f-b3fd-21d6745f7f52)

When approximating the square root function using Newton's method, the function $f(x) = x^2 - S$, and $f'(x) = 2x$. To find the final function and minimize the floating point operations ([FLOPS](https://en.wikipedia.org/wiki/FLOPS)) from 5 to 3, the function will become to a following form:

$$
\begin{aligned}
x_{n+1}
&= x_n - \frac{f(x_n)}{f'(x_n)} \\
&= x_n - \frac{x_n^2 - S}{2x} \\
&= \frac{2x_n^2 - x_n^2 + S}{2x} \\
&= \frac{x_n^2 + S}{2x} \\
&= \frac{x_n}{2} + \frac{S}{2x_n} \\
&= \frac{x_n + \frac{S}{x_n}}{2}. \\
\end{aligned}
$$

A good initial value for the whole value range is

$$
x_0 = \frac{S}{2},
$$

where $S$ is the input digit. However, to get an accurate result with this initial value, it will require 10 iterations to get <1 % maximum error. To approximate the answer faster, one could setup a small LUT for a more accurate initial value.

The LUT I have manually created, includes 8 division factors $d$ requiring 4 FLOPS in total to set the initial value. 3 FLOPS is used for finding the right division factor with [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm) and 1 flop is used for the division

$$
x_0 = \frac{S}{d}.
$$

Executing one iteration of Newton-Raphson method requires 3 FLOPS. In this setup, 2 to 3 iterations were enough to approximate logarithm. See the statistics in the table and approximation accuracy in the figure.

| Iterations | Average error | Max error | OPS                |
|------------|---------------|-----------|--------------------|
| 2          | 0.16 %        | 6.98 %    | 2 * 3 + 4 = **10** |
| 3          | 0.00001 %     | 0.23 %    | 3 * 3 + 4 = **13** |

![Approximation errors](https://github.com/pettod/cs-basics/assets/33998401/3cbc7830-d10a-4873-bbfc-455d8bc960c2)

## Sigmoid approximation and

## Merge sort

Recursive merge sort. Graphs show the time complexity.

![measurements](https://github.com/pettod/merge-sort/assets/33998401/26d45a62-c7aa-4397-be0e-de050021b0ee)
