import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import functions as functions  
import simulations as sim



def analyze_normalized_tau_total(node_sizes, num_simulations, fragmentation_rate, coagulation_rate):
    results = {}
    for n in node_sizes:
        tau_totals = functions.simulate_tau_total(num_simulations, n, fragmentation_rate, coagulation_rate)
        mean_tau = np.mean(tau_totals)
        var_tau = np.var(tau_totals)
        std_tau = np.sqrt(var_tau)
        # Compute harmonic number
        H_n = functions.harmonic(n)
        # Normalized Z
        Z = (tau_totals - mean_tau) / std_tau  # Use empirical scaling
        results[n] = {"Z": Z, "mean_tau": mean_tau, "var_tau": var_tau}
    return results

# Parameters
node_sizes = [10, 100, 500]
num_simulations = 1000
fragmentation_rate = 1.0
coagulation_rate = 2.0


#Plotting
results = analyze_normalized_tau_total(node_sizes, num_simulations, fragmentation_rate, coagulation_rate)


plt.figure(figsize=(12, 6))
colors = ['blue', 'orange', 'green']

for i, n in enumerate(node_sizes):
    Z = results[n]["Z"]
    plt.hist(Z, bins=30, alpha=0.5, label=f"n = {n}", color=colors[i], density=True)

x = np.linspace(-4, 4, 500)
plt.plot(x, norm.pdf(x), 'k--', label="Standard Normal (N(0,1))")

plt.title("Distribution of Normalized Tau Total (Z)")
plt.xlabel("Z")
plt.ylabel("Density")
plt.legend()
plt.show()

for n in node_sizes:
    print(f"n = {n}: Mean = {results[n]['mean_tau']:.3f}, Variance = {results[n]['var_tau']:.3f}")
