from sorting_algorithms import merge_sort
from sorting_algorithms import quick_sort
import timeit
import matplotlib.pyplot as plt
import numpy as np

m, M, n, N, o, O, p, P, q = 10000, 20000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 35000000 #sizes of n to be tested for

# define the n sizes in an array
sizes = [m, M, n, N, o, O, p, P, q]

print("Test Sorting Algorithms, Tower of Hanoi Algorithm, or Classical and Strassen’s Matrix Multiplication.")
while True:
    algorithms = input("\nType Sorting, Tower, or Matrix to Proceed. Type End to exit: ")

    if algorithms.casefold() == "end":
        print("Exiting Test.")
        break

    elif algorithms.casefold() == "sorting":

        # creates random integer arrays based on the different sizes of n
        rng = np.random.default_rng()
        mergeS_m = rng.integers(low=-35000000, high=35000000, size=m)
        mergeS_M = rng.integers(low=-35000000, high=35000000, size=M)
        mergeS_n = rng.integers(low=-35000000, high=35000000, size=n)
        mergeS_N = rng.integers(low=-35000000, high=35000000, size=N)
        mergeS_o = rng.integers(low=-35000000, high=35000000, size=o)
        mergeS_O = rng.integers(low=-35000000, high=35000000, size=O)
        mergeS_p = rng.integers(low=-35000000, high=35000000, size=p)
        mergeS_P = rng.integers(low=-35000000, high=35000000, size=P)
        mergeS_q = rng.integers(low=-35000000, high=35000000, size=q)

        quickS_m = rng.integers(low=-35000000, high=35000000, size=m)
        quickS_M = rng.integers(low=-35000000, high=35000000, size=M)
        quickS_n = rng.integers(low=-35000000, high=35000000, size=n)
        quickS_N = rng.integers(low=-35000000, high=35000000, size=N)
        quickS_o = rng.integers(low=-35000000, high=35000000, size=o)
        quickS_O = rng.integers(low=-35000000, high=35000000, size=O)
        quickS_p = rng.integers(low=-35000000, high=35000000, size=p)
        quickS_P = rng.integers(low=-35000000, high=35000000, size=P)
        quickS_q = rng.integers(low=-35000000, high=35000000, size=q)

        # standard Python lists from NumPy arrays
        arrays_to_test = [
            mergeS_m.tolist(),
            mergeS_M.tolist(),
            mergeS_n.tolist(),
            mergeS_N.tolist(),
            mergeS_o.tolist(),
            mergeS_O.tolist(),
            mergeS_p.tolist(),
            mergeS_P.tolist(),
            mergeS_q.tolist()
        ]

        merge_times = []
        quick_times = []

        print("Timing algorithms (this may take a moment)...")

        # time both algorithms for each size
        for i, arr in enumerate(arrays_to_test):
            current_size = sizes[i]

            # time Merge Sort (run 3 times and take the average)
            t_merge = timeit.timeit(lambda: merge_sort(arr), number=1)
            merge_times.append(t_merge)

            # time Quick Sort (must copy array)
            t_quick = timeit.timeit(lambda: quick_sort(arr.copy(), 0, current_size - 1), number=1)
            quick_times.append(t_quick)

        # plot results
        plt.figure(figsize=(10, 6))
        plt.plot(sizes, merge_times, label='Merge Sort', marker='o', linewidth=2)
        plt.plot(sizes, quick_times, label='Quick Sort', marker='s', linewidth=2)

        plt.title('Merge Sort vs. Quick Sort Execution Time')
        plt.xlabel('Array Size (N)')
        plt.ylabel('Time (Seconds)')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)

        # show graph window
        plt.ticklabel_format(style='plain', axis='x')
        plt.show()
        break

    elif algorithms.casefold() == "tower":
        print("Tower")
        break

    elif algorithms.casefold() == "matrix":
        print("Matrix.")
        break

    else:
        print("Invalid Input. Please try again.")
        continue


    #print("Merge Sort, Size n = 10,000:", np.array(merge_sort(mergeS_m)))
#print("Merge Sort, Size n = 20,000:", np.array(merge_sort(mergeS_M)))
#print("Merge Sort, Size n = 50,000:", np.array(merge_sort(mergeS_n)))
#print("Merge Sort, Size n = 100,000:", np.array(merge_sort(mergeS_N)))
#print("Quick Sort, Size n = 10,000:", quick_sort(quickS_m, 0, len(quickS_m)-1))
#print("Quick Sort, Size n = 20,000:", quick_sort(quickS_M, 0, len(quickS_M)-1))
#print("Quick Sort, Size n = 50,000:", quick_sort(quickS_n, 0, len(quickS_n)-1))
#print("Quick Sort, Size n = 100,000:", quick_sort(quickS_N, 0, len(quickS_N)-1))
