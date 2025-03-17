"""
This program simulates multiple coin toss experiments to analyze the distribution of heads.
It performs N experiments, each consisting of n fair coin tosses, counts the number of heads,
computes the percentage of heads for each experiment, and plots a histogram of these percentages.
Progress updates are printed every 10% of the iterations.
"""

import numpy as np
import matplotlib.pyplot as plt

# Set parameters
N = 10000  # number of experiments
n = 100   # number of tosses per experiment

# Initialize array to store the number of heads for each experiment
heads_counts = np.zeros(N, dtype=int)

# Simulate the experiments
for i in range(N):
    # Simulate n fair coin tosses and count heads using binomial distribution
    heads_counts[i] = np.random.binomial(n, 0.5)
    # Print progress updates every 10% of iterations
    if (i + 1) % (N // 10) == 0:
        print(f"{(i + 1) / N * 100:.0f}% completed")

# Compute the percentage of heads for each experiment
percentages = (heads_counts / n) * 100

# Plot the histogram of the percentage of heads
plt.hist(percentages, bins=20)
plt.xlabel("Percentage of Heads")
plt.ylabel("Frequency")
plt.title("Grok")
plt.show()