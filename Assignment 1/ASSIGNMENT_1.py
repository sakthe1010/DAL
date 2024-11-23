import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading data from csv file
df = pd.read_csv("House_Dataset.csv")

# Converting data into matrix
matrix = df.values

# Creating zero matrix
zero_matrix = np.zeros((10000,10000))

# Filling the matrix
for i in range(len(matrix)):
    a = int(matrix[i][0])
    b = int(matrix[i][1])
    zero_matrix[a][b] = 1

# Creating rotated and mirrored matrices
rot90_matrix = np.rot90(zero_matrix,3)
mirror_matrix = np.flipud(np.rot90(zero_matrix,2))

# Finding the coordinates of 1's in each matrix
rot_rows,rot_cols = np.where(rot90_matrix == 1)
mirror_rows,mirror_cols = np.where(mirror_matrix == 1)

# Plotting the matrices
plt.scatter(rot_rows,rot_cols,color = 'blue')
plt.show()
plt.scatter(mirror_rows,mirror_cols,color = 'red')
plt.show()