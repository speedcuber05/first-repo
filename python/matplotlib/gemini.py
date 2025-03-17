import numpy as np
import matplotlib.pyplot as plt

def coin_toss_experiments(N, n):
    """
    Simulates multiple coin toss experiments and analyzes the distribution of heads.

    Args:
        N (int): The number of experiments to perform.
        n (int): The number of coin tosses in each experiment.

    Returns:
        numpy.ndarray: An array containing the percentage of heads observed in each experiment.
    """

    results = np.zeros(N)  # Array to store the percentage of heads for each experiment

    for i in range(N):
        tosses = np.random.randint(0, 2, n)  # 0 represents tails, 1 represents heads
        heads = np.sum(tosses)
        results[i] = (heads / n) * 100  # Store the percentage of heads

        # Print progress updates
        if (i + 1) % (N // 10) == 0:
            print(f"Progress: {((i + 1) / N) * 100:.1f}% complete")

    return results

def plot_histogram(data):
    """
    Plots a histogram of the given data.

    Args:
        data (numpy.ndarray): The data to plot.
    """

    plt.hist(data, bins=20, edgecolor='black')
    plt.title("Gemini")
    plt.xlabel("Percentage of Heads")
    plt.ylabel("Frequency")
    plt.show()

if __name__ == "__main__":
    N = 10000  # Number of experiments
    n = 100  # Number of tosses per experiment

    print(f"Simulating {N} experiments with {n} tosses each...")

    results = coin_toss_experiments(N, n)

    print("Simulation complete.")

    plot_histogram(results)