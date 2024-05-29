import time
import multiprocessing
import numpy as np
import matplotlib.pyplot as plt

def multiply_row(args):
    row_a, matrix_b = args
    return [sum(a*b for a, b in zip(row_a, col_b)) for col_b in zip(*matrix_b)]

def matrix_multiply(matrix_a, matrix_b):
    return list(map(multiply_row, [(row_a, matrix_b) for row_a in matrix_a]))

def parallel_matrix_multiply(matrix_a, matrix_b):
    with multiprocessing.Pool() as pool:
        return pool.map(multiply_row, [(row_a, matrix_b) for row_a in matrix_a])

def numpy_matrix_multiply(matrix_a, matrix_b):
    return np.dot(matrix_a, matrix_b)

def main():
    matrix_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    standard_times = []
    parallel_times = []
    numpy_times = []

    for size in matrix_sizes:
        matrix_a = [[1]*size for _ in range(size)]
        matrix_b = [[1]*size for _ in range(size)]

        start_time = time.time()
        matrix_multiply(matrix_a, matrix_b)
        end_time = time.time()
        standard_times.append(end_time - start_time)

        start_time = time.time()
        parallel_matrix_multiply(matrix_a, matrix_b)
        end_time = time.time()
        parallel_times.append(end_time - start_time)

        start_time = time.time()
        numpy_matrix_multiply(np.array(matrix_a), np.array(matrix_b))
        end_time = time.time()
        numpy_times.append(end_time - start_time)

    plt.plot(matrix_sizes, standard_times, label="Standard")
    plt.plot(matrix_sizes, parallel_times, label="Parallel")
    plt.plot(matrix_sizes, numpy_times, label="NumPy")
    plt.xlabel("Matrix Size")
    plt.ylabel("Time (seconds)")
    plt.title("Matrix Multiplication Performance")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()