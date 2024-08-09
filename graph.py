import matplotlib.pyplot as plt
sizes = [100, 1000, 5000, 10000, 50000, 100000]
selection_times = [0.000123, 0.002345, 0.012345, 0.045678, 0.234567, 0.567890]
bubble_times = [0.000256, 0.003678, 0.013678, 0.067890, 0.345678, 0.678901]
insertion_times = [0.000145, 0.002456, 0.012456, 0.045789, 0.234789, 0.567901]
quick_times = [0.000056, 0.001234, 0.006789, 0.023456, 0.123456, 0.345678]
merge_times = [0.000089, 0.001678, 0.007123, 0.024567, 0.125678, 0.349012]
plt.figure(figsize=(12, 10))
plt.plot(sizes, selection_times, marker='*', linestyle='-', color='blue', label='Selection Sort', linewidth=2)
plt.plot(sizes, bubble_times, marker='.', linestyle='--', color='red', label='Bubble Sort', linewidth=2)
plt.plot(sizes, insertion_times, marker='o', linestyle='-.', color='green', label='Insertion Sort', linewidth=2)
plt.plot(sizes, quick_times, marker='v', linestyle=':', color='purple', label='Quick Sort', linewidth=2)
plt.plot(sizes, merge_times, marker='^', linestyle='-', color='orange', label='Merge Sort', linewidth=2)
plt.title('Sorting Algorithm Time Complexity', fontsize=20, fontweight='bold', color='navy')
plt.xlabel('Array Size', fontsize=16, fontweight='bold')
plt.ylabel('Time (seconds)', fontsize=16, fontweight='bold')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend(fontsize=12, shadow=True)
plt.show()

