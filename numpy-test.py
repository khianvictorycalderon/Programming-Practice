import numpy as np

# Sample data
arr = np.array([4, 2, 6, 4, 7, 3, 1, 5, 7, 3, 3, 1, 6, 8, 2, 9, 4])

# Get the mean
manual_mean = np.sum(arr) / len(arr)
print(f"Manual mean is {manual_mean}")
automated_mean = np.mean(arr)
print(f"Automated mean is {automated_mean}")

# Get the median
median = np.median(arr)
print(f"Median is {median}")