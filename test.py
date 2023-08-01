import numpy as np

# Create an empty array to store the stacked arrays
stacked_arrays = np.empty((0, 3))  # shape (0, 3) means 0 rows and 3 columns

# Loop over some arrays and add them to the stacked array
for i in range(3):
    arr = np.random.rand(1, 3)  # create a random 1x3 array
    stacked_arrays = np.vstack((stacked_arrays, arr))  # add the array to the stacked array
    

# Print the stacked array
print(stacked_arrays)
