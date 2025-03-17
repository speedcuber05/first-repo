import numpy as np
import matplotlib.pyplot as plt

# Get user inputs for the number of experiments and tosses per experiment
N = int(input("Enter the number of experiments (N): "))
n = int(input("Enter the number of tosses per experiment (n): "))

# Validate input values
if N <= 0 or n <= 0:
    raise ValueError("N and n must be positive integers.")

# Initialize an array to store the number of heads in each experiment
heads = np.zeros(N, dtype=int)

# Progress tracking variables
next_percent = 10  # Next progress milestone to print
print("Starting simulations...")

# Perform each experiment and track progress
for i in range(N):
    # Simulate 'n' coin tosses and count heads using binomial distribution
    heads[i] = np.random.binomial(n, 0.5)
    
    # Calculate current progress percentage
    current_progress = (i + 1) / N * 100
    
    # Print progress if current progress meets or exceeds the next milestone
    if current_progress >= next_percent:
        print(f"{next_percent:.0f}% completed")
        next_percent += 10

# Calculate the percentage of heads for each experiment
percent_heads = (heads / n) * 100

# Create and customize the histogram
plt.figure(figsize=(10, 6))
plt.hist(percent_heads, bins=20, edgecolor='black', alpha=0.7, color='skyblue')
plt.title('Deekseek')
plt.xlabel('Percentage of Heads')
plt.ylabel('Number of Experiments')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()