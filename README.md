# Random Point Sampling for Soil Analysis

This program is a part of a capstone project involving a rover designed for collecting soil samples for analysis. It implements an algorithm that randomly chooses 5 points within a 1-acre square land.

## Algorithm Explanation

The algorithm works as follows:

1. Randomly chooses a point within a 10x10 grid.
2. Vertically divides the land and chooses the second point randomly in the half where the first point is not located.
3. Horizontally divides the land and chooses the third point randomly in the half where the first point is not located.
4. The fourth point is taken on one of the vertical borders.
5. The fifth point is taken on one of the horizontal borders.

The implementation of this algorithm can be found in the file `RandomPointSimulation.py`.

## Standard Deviation Analysis

In the `StandardDeviationScale.py` file, the above algorithm is run 100 times. During each iteration, 5 points are found, and the distances between them are calculated, along with their standard deviation. These values are then plotted on a line. This analysis helps in understanding both the worst-case scenario (where points are not well spaced) and the best-case scenario. 

This information is invaluable for automating the process of finding soil sampling sites, a critical aspect of soil sampling where both random and well-spaced sites are essential for accurate results.

The program aims to improve the efficiency and precision of soil sampling for more reliable soil analysis, which is crucial for various applications, from agriculture to environmental science. 

Feel free to explore and use the code to enhance your own projects related to soil analysis and sampling.
