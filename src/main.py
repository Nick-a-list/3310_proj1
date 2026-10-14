from sorting_algorithms import merge_sort
from sorting_algorithms import quick_sort
from matrix_multiplication import classical_multiply, strassen_multiply
from tower_hanoi import tower_of_hanoi
import timeit
import matplotlib.pyplot as plt
import numpy as np

print("Test Sorting Algorithms, Tower of Hanoi Algorithm, or Classical and Strassen’s Matrix Multiplication.")
while True:
    algorithms = input("\nType Sorting, Tower, or Matrix to Proceed. Type End to exit: ")

    if algorithms.casefold() == "end":
        print("Exiting Test.")
        break

    elif algorithms.casefold() == "sorting":
        m, M, n, N, o, O, p, P, q = 10000, 20000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 35000000  # sizes of n to be tested for

        # define the n sizes in an array
        sizes = [m, M, n, N, o, O, p, P, q]
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
            print(f"\nTesting n = {current_size}...")

            # time Merge Sort (run 1 time)
            t_merge = timeit.timeit(lambda: merge_sort(arr), number=1)
            merge_times.append(t_merge)
            print(f"Merge Sort completed in {t_merge:.4f} seconds.")

            # time Quick Sort (must copy array)
            t_quick = timeit.timeit(lambda: quick_sort(arr.copy(), 0, current_size - 1), number=1)
            quick_times.append(t_quick)
            print(f"Quick Sort completed in {t_quick:.4f} seconds.")

            # checking time limit (if either algorithm takes more than 5 minutes),
            # the next size will likely exceed the 10-minute limit O(N Log N)
            if t_merge > 300.0 or t_quick > 300.0:
                print(f"\nStopping sorting test early. The next size will exceed the 10-minute limit.")
                # slice array so Matplotlib only graphs the finished ones
                sizes = sizes[:len(merge_times)]
                break

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
        tower_sizes = [2, 4, 8, 16, 20, 24, 28, 32]
        tower_times = []

        print("\nTiming Tower of Hanoi...")
        for size in tower_sizes:
            print(f"Testing n = {size}...")

            # time the recursive function
            t_tower = timeit.timeit(lambda: tower_of_hanoi(size, 'A', 'C', 'B'), number=1)
            tower_times.append(t_tower)

            print(f"Completed in {t_tower:.4f} seconds.")

            # growth is 2^n
            # if n=32 takes ~30 seconds, n=36 would take ~8 minutes. stops at 120 seconds.
            if t_tower > 120.0:
                print(f"\nStopping testing. Next size will exceed the 10-minute limit.")
                # Slice the sizes array to match the recorded times before plotting
                tower_sizes = tower_sizes[:len(tower_times)]
                break

        # plot results
        plt.figure(figsize=(10, 6))
        plt.plot(tower_sizes, tower_times, label='Tower of Hanoi', marker='^', color='red', linewidth=2)

        plt.title('Tower of Hanoi Execution Time (Exponential Growth)')
        plt.xlabel('Number of Disks (N)')
        plt.ylabel('Time (Seconds)')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()
        break

    elif algorithms.casefold() == "matrix":
        # powers of 2
        matrix_sizes = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

        classical_times = []
        strassen_times = []
        rng = np.random.default_rng()

        print("\nTiming Matrix Multiplication Algorithms...")
        for size in matrix_sizes:
            print(f"\nTesting n = {size}x{size}...")

            # generate two random n x n matrices
            # convert them to lists
            A = rng.integers(low=-100, high=100, size=(size, size)).tolist()
            B = rng.integers(low=-100, high=100, size=(size, size)).tolist()

            # time classical multiplication
            t_class = timeit.timeit(lambda: classical_multiply(A, B), number=1)
            classical_times.append(t_class)
            print(f"Classical completed in {t_class:.4f} seconds.")

            # time strassen's multiplication
            t_stras = timeit.timeit(lambda: strassen_multiply(A, B), number=1)
            strassen_times.append(t_stras)
            print(f"Strassen completed in {t_stras:.4f} seconds.")

            # matrix multiplication scales (O(n^3)).
            # to prevent going over 10 minutes, check both strassen and classical
            if t_class > 120.0 or t_stras > 120.0:
                print(f"\nStopping testing early. The next size will exceed the 10-minute limit.")
                matrix_sizes = matrix_sizes[:len(classical_times)]
                break

        # plot results
        plt.figure(figsize=(10, 6))
        plt.plot(matrix_sizes, classical_times, label='Classical ($O(n^3)$)', marker='o', linewidth=2)
        plt.plot(matrix_sizes, strassen_times, label='Strassen ($O(n^{2.81})$)', marker='s', linewidth=2)

        plt.title('Classical vs. Strassen Matrix Multiplication')
        plt.xlabel('Matrix Size (N x N)')
        plt.ylabel('Time (Seconds)')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()
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
