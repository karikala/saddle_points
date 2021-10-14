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
def main():
  matrix =[]
  n = int(input("Enter the n (rows and columns) of square matrix: "))
  for i in range(n):
    sublis=[]
    for j  in range(n):
      sublis.append(int(input()))
    matrix.append(sublis)
  return matrix, n

def saddle_point(mat,n):
  for i in range(n):
    row_min = mat[i][0]
    col_ind = 0
    for j in range(n):
      if(row_min > mat[i][j]):
        row_min = mat[i][j]
        col_ind = j
    m=0
    for k in range(n):
      if(row_min<mat[k][col_ind]):
        break
      m+=1
    if(n==m):
      print(str(row_min),"is Saddle point\n")
      print("coordinates are({0},{1})".format(i,j))
      


if __name__ == "__main__" :
  mat, n =main()
  print(mat,n)
  saddle_point(mat,n)