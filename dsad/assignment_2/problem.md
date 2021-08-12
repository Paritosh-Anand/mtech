## Problem Statement
The city planning committee of city X needs to create a plan to establish fire stations at specific locations. The planning committee has formed a task force to:

find the optimal positions for the fire stations by considering the matrices like fire risk matrix, travel time matrix etc. 

As part of finding the optimal firehouse locations the task forces needs to find the most efficient way to multiply these matrices together. 

The efficient way is the one that involves the minimum number of multiplications. 
The dimensions of the matrices are given in an array a[] of size N (such that N = number of matrices + 1) where the ith matrix has the dimensions (a[i-1] x a[i]).

## Requirements:

1. Formulate an efficient algorithm to perform the above task to help the task force such that:
    the value N and the array a[] are taken as input parameters 
    and the minimum number of multiplication operations needed to be performed is returned.
2. Provide a description about the design strategy used.
3. Analyse the time complexity of the algorithm and show that it is an “efficient” one.
4. Implement the above problem statement using Python 3.7