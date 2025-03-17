import numpy as np
import matplotlib.pyplot as plt

# Set parameters for the simulation
N = 10000   # Total number of experiments
n = 100     # Number of coin tosses in each experiment

# List to store the percentage of heads for each experiment
percentage_heads = []

# Calculate how many experiments correspond to a 10% progress update.
# Use max to ensure we update at least every experiment if N < 10.
progress_step = max(N // 10, 1)

# Loop over the number of experiments
for i in range(N):
    # Simulate coin tosses using the binomial distribution.
    # np.random.binomial(n, 0.5) simulates n tosses with a probability of 0.5 for heads,
    # and returns the number of heads.
    heads = np.random.binomial(n, 0.5)

    # Calculate the percentage of heads in this experiment
    percent = (heads / n) * 100
    percentage_heads.append(percent)
    
    
    # Print progress updates every 10% of the total experiments
    if (i + 1) % progress_step == 0:
        progress = int((i + 1) / N * 100)
        print(f"Progress: {progress}% of experiments completed.")

# Convert list to a NumPy array for further analysis if needed
percentage_heads = np.array(percentage_heads)

# Plotting the histogram of the percentage of heads
plt.figure(figsize=(10, 6))
plt.hist(percentage_heads, bins=20, color='skyblue', edgecolor='black')
plt.title("ChatGPT")
plt.xlabel("Percentage of Heads (%)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
