import numpy as np

def strassen(A, B):
    n = A.shape[0]
    if n == 1:
        return A * B
    
    # Padding matrices to the nearest power of 2
    m = 1 << (n-1).bit_length()
    A_pad = np.pad(A, ((0, m-n), (0, m-n)), mode='constant')
    B_pad = np.pad(B, ((0, m-n), (0, m-n)), mode='constant')
    
    # Recursive step
    k = m // 2
    A11, A12, A21, A22 = A_pad[:k,:k], A_pad[:k,k:], A_pad[k:,:k], A_pad[k:,k:]
    B11, B12, B21, B22 = B_pad[:k,:k], B_pad[:k,k:], B_pad[k:,:k], B_pad[k:,k:]
    
    # Computing the 7 products
    P1 = strassen(A11 + A22, B11 + B22)
    P2 = strassen(A21 + A22, B11)
    P3 = strassen(A11, B12 - B22)
    P4 = strassen(A22, B21 - B11)
    P5 = strassen(A11 + A12, B22)
    P6 = strassen(A21 - A11, B11 + B12)
    P7 = strassen(A12 - A22, B21 + B22)
    
    # Computing the resulting quadrants
    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 - P2 + P3 + P6
    
    # Combining the quadrants into the result matrix
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    
    # Removing the padding
    return C[:n,:n]

# Helper function to generate random matrices
def random_matrix(n):
    return np.random.randint(0, 10, size=(n, n))

# Test the Strassen algorithm
def test_strassen(n):
    A = random_matrix(n)
    B = random_matrix(n)
    
    C_strassen = strassen(A, B)
    C_numpy = A @ B
    
    assert np.allclose(C_strassen, C_numpy), "Strassen's algorithm implementation is incorrect"
    
    print(f"Strassen's algorithm works correctly for {n}x{n} matrices")

# Analyze the complexity
def analyze_complexity(n_values):
    import timeit
    
    def wrapper(func, *args, **kwargs):
        def wrapped():
            return func(*args, **kwargs)
        return wrapped
    
    for n in n_values:
        A = random_matrix(n)
        B = random_matrix(n)
        
        strassen_wrapped = wrapper(strassen, A, B)
        numpy_wrapped = wrapper(np.dot, A, B)
        
        strassen_time = timeit.timeit(strassen_wrapped, number=1)
        numpy_time = timeit.timeit(numpy_wrapped, number=1)
        
        print(f"n = {n}")
        print(f"Strassen's algorithm time: {strassen_time:.5f} seconds")
        print(f"NumPy dot product time: {numpy_time:.5f} seconds")
        print(f"Speedup: {numpy_time / strassen_time:.2f}x")
        print()

# Run the tests and analysis
# test_strassen(64)
# test_strassen(128)
# test_strassen(256)

# n_values = [64, 128, 256, 512]
# analyze_complexity(n_values)

# User input
if __name__ == "__main__":
    n = int(input("Enter the size of the matrix: "))
    A = random_matrix(n)
    B = random_matrix(n)
    C = strassen(A, B)
    print("Resulting matrix:")
    print(C)

    test_strassen(n)
    analyze_complexity([n])