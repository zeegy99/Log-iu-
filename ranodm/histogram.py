from tester import *
import matplotlib.pyplot as plt

n = 10000

values = []
all_longest_times = []  # To store longest_times from all trials

# Run 100 trials
for i in range(n):
    _, _, _, longest_times = main(15)  # Unpack only the longest_times
    all_longest_times.extend(longest_times)  # Append the longest_times from this trial to the overall list

# Determine the final reproduction time for bins
final_reproduction_time = max(all_longest_times)  # Use the maximum for bin creation

# Create bins ranging from 0 to final_reproduction_time with a step of 0.1
bins = [round(x * 0.1, 2) for x in range(int(final_reproduction_time * 10) + 1)]

# Count frequencies
frequency = [0] * (len(bins) - 1)  # Adjust length to bins - 1

# Populate frequency counts
for time in all_longest_times:
    for j in range(len(bins) - 1):  # Iterate over bins
        if bins[j] <= time < bins[j + 1]:
            frequency[j] += 1
            break

# Plotting the histogram
plt.figure(figsize=(10, 6))
plt.bar(bins[:-1], frequency, width=0.1, align='edge', color='lightblue', edgecolor='black')
plt.xlabel('Time of final baby')
plt.ylabel('Frequency')
plt.title(f'Histogram of Final Node Spawn Times over {n} Trials')
plt.xticks(bins, rotation=45)  # Rotate x-axis labels for better visibility
plt.grid(axis='y')
plt.show()
