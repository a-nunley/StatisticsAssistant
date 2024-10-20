# Author: A-Nunley
# Date: 10/19/2024
# File: X-barandRCharts.py
#
# This program calculates the X-bar and R charts for a given set of samples.
import numpy as np
import matplotlib.pyplot as plt

# Prompt user for parameters
num_samples = int(input("Enter the number of samples: "))
sample_size = int(input("Enter the sample size: "))
mean = float(input("Enter the mean of the distribution: "))
std_dev = float(input("Enter the standard deviation of the distribution: "))

# Set random seed for reproducibility
np.random.seed(42)

# Generate samples
samples = np.random.normal(loc=mean, scale=std_dev, size=(num_samples, sample_size))

# Calculate X-bar and R
x_bar = samples.mean(axis=1)
R = samples.max(axis=1) - samples.min(axis=1)

# Calculate control limits for X-bar chart
x_bar_mean = np.mean(x_bar)
R_mean = np.mean(R)
UCL_X = x_bar_mean + 1.96 * (R_mean / np.sqrt(sample_size))
LCL_X = x_bar_mean - 1.96 * (R_mean / np.sqrt(sample_size))

# Calculate control limits for R chart
UCL_R = R_mean * 2
LCL_R = max(0, R_mean - 2)

# Plot X-bar chart
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(x_bar, marker='o', linestyle='-', color='b', label='X-bar')
plt.axhline(UCL_X, color='r', linestyle='--', label='UCL')
plt.axhline(LCL_X, color='r', linestyle='--', label='LCL')
plt.axhline(x_bar_mean, color='g', linestyle='-', label='Mean')
plt.title('X-bar Chart')
plt.legend()

# Plot R chart
plt.subplot(2, 1, 2)
plt.plot(R, marker='o', linestyle='-', color='b', label='Range')
plt.axhline(UCL_R, color='r', linestyle='--', label='UCL')
plt.axhline(LCL_R, color='r', linestyle='--', label='LCL')
plt.axhline(R_mean, color='g', linestyle='-', label='Mean')
plt.title('R Chart')
plt.legend()

# Adjust layout and show plot
plt.tight_layout()
plt.show()