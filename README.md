# saddle_points
"""
Saddle points:
Given a matrix of n x n size, the task is to find the saddle point of the matrix. A saddle point is an element of the matrix such that it is the minimum element in its row and maximum in its column. 
Examples : 
 

Input: Mat[3][3] = { {1, 2, 3},
                  {4, 5, 6},
                  {7, 8, 9}}
Output: 7
7 is minimum in its row and maximum in its column.

Input: Mat[3][3] = {{1, 2, 3},
                    {4, 5, 6},
                    {10, 18, 4}}
Output: No saddle point
Find the minimum element of the current row and store the column index of the minimum element.
Check if the row minimum element is also maximum in its column. We use the stored column index here.
If yes, then saddle point else continues till the end of the matrix

"""
