
import networkx as nx
import numpy as np
import functions as functions 
import matplotlib.pyplot as plt




# Parameters
num_simulations = 10
fragmentation_rate = 0.5
coagulation_rate = 2.0
node_sizes = [10] #simulation




#Plotting
plt.figure(figsize=(12, 8))

for n in node_sizes:
    Z = functions.simulate_normalized_tau_total(num_simulations, n, fragmentation_rate, coagulation_rate)
    plt.hist(Z, bins=30, alpha=0.5, label=f"n = {n}", edgecolor='black')



plt.title(r"Distribution of $\frac{\tilde{\tau}_{\text{total}} - 2H_n}{\sqrt{\text{Var}(\tilde{\tau}_{\text{total}})}}$")
plt.xlabel("Z")
plt.ylabel("Frequency")
plt.legend()
plt.show()

