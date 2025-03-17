import numpy as np
import matplotlib.pyplot as plt
from time import time

def coin_toss_simulation(n_tosses, n_experiments):
    """
    Simulates multiple coin toss experiments and analyzes the distribution of heads.
    
    Parameters:
    n_tosses (int): Number of coin tosses in each experiment
    n_experiments (int): Number of experiments to run
    
    Returns:
    numpy.ndarray: Array containing the percentage of heads in each experiment
    """
    # Initialize array to store results (percentage of heads in each experiment)
    results = np.zeros(n_experiments)
    
    # Track start time for performance monitoring
    start_time = time()
    
    # Run experiments
    for i in range(n_experiments):
        # Simulate n_tosses coin tosses (0 for tails, 1 for heads)
        tosses = np.random.randint(0, 2, n_tosses)
        
        # Calculate percentage of heads
        percentage_heads = np.sum(tosses) / n_tosses * 100
        
        # Store result
        results[i] = percentage_heads
        
        # Print progress updates at every 10% of iterations
        if (i + 1) % (n_experiments // 10) == 0 or i == n_experiments - 1:
            progress = (i + 1) / n_experiments * 100
            elapsed_time = time() - start_time
            print(f"Progress: {progress:.1f}% complete. Elapsed time: {elapsed_time:.2f} seconds")
    
    return results

def plot_results(results, n_tosses, n_experiments):
    """
    Plots a histogram of the results.
    
    Parameters:
    results (numpy.ndarray): Array containing the percentage of heads in each experiment
    n_tosses (int): Number of coin tosses in each experiment
    n_experiments (int): Number of experiments run
    """
    plt.figure(figsize=(10, 6))
    
    # Calculate theoretical mean and standard deviation
    theoretical_mean = 50.0  # Expected percentage of heads for a fair coin
    theoretical_std = np.sqrt(n_tosses * 0.5 * 0.5) / n_tosses * 100  # Standard deviation in percentage
    
    # Calculate bin width for histogram - adjust based on the standard deviation
    bin_width = max(0.5, theoretical_std / 4)  # Ensure bins aren't too narrow
    bin_range = (theoretical_mean - 4 * theoretical_std, theoretical_mean + 4 * theoretical_std)
    bins = np.arange(bin_range[0], bin_range[1] + bin_width, bin_width)
    
    # Plot histogram
    plt.hist(results, bins=bins, alpha=0.7, color='skyblue', edgecolor='black')
    
    # Add vertical line for theoretical mean
    plt.axvline(theoretical_mean, color='red', linestyle='dashed', linewidth=1.5, 
                label=f'Theoretical Mean: {theoretical_mean}%')
    
    # Add vertical lines for observed mean and standard deviation
    observed_mean = np.mean(results)
    observed_std = np.std(results)
    plt.axvline(observed_mean, color='green', linestyle='dashed', linewidth=1.5,
                label=f'Observed Mean: {observed_mean:.2f}%')
    
    # Add annotations for standard deviation
    plt.annotate(f'Theoretical StdDev: {theoretical_std:.2f}%', 
                 xy=(0.05, 0.95), xycoords='axes fraction', ha='left', va='top')
    plt.annotate(f'Observed StdDev: {observed_std:.2f}%', 
                 xy=(0.05, 0.90), xycoords='axes fraction', ha='left', va='top')
    
    # Set plot title and labels
    plt.title('Claude')
    plt.xlabel('Percentage of Heads (%)')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Show the plot
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to run the simulation with user inputs.
    """
    print("Coin Toss Simulation")
    print("====================")
    
    # Get user inputs with default values
    try:
        n_tosses = int(input("Enter number of tosses per experiment [default: 100]: ") or 100)
        n_experiments = int(input("Enter number of experiments to run [default: 10000]: ") or 10000)
    except ValueError:
        print("Invalid input. Using default values.")
        n_tosses = 100
        n_experiments = 10000
    
    # Run simulation
    print(f"\nRunning {n_experiments} experiments with {n_tosses} tosses each...")
    results = coin_toss_simulation(n_tosses, n_experiments)
    
    # Display summary statistics
    print("\nSummary Statistics:")
    print(f"Mean percentage of heads: {np.mean(results):.2f}%")
    print(f"Standard deviation: {np.std(results):.2f}%")
    print(f"Minimum percentage: {np.min(results):.2f}%")
    print(f"Maximum percentage: {np.max(results):.2f}%")
    
    # Plot results
    plot_results(results, n_tosses, n_experiments)

if __name__ == "__main__":
    main()