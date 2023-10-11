# Three ways of multiplying Matrices

# importing numpy
import numpy as np

np.random.seed(28)

A = np.random.randint(1, 10, size=(3, 3))
B = np.random.randint(1, 10, size=(3, 2))

print(f"Matrix A: \n {A}\n")
print(f"Matrix B: \n {B}\n")


# Custom function to multiply matrices
def multiply_matrix(A, B):
    global C
    if A.shape[1] == B.shape[0]:
        C = np.zeros((A.shape[0], B.shape[1]), dtype=int)
        for row in range(A.shape[0]):
            for col in range(B.shape[1]):
                for elt in range(len(B)):
                    C[row, col] += A[row, elt] * B[elt, col]
        return C
    else:
        return "Sorry, cannot multiply A and B."


print("Custom code")
print(multiply_matrix(A, B))

# Multiplying matrices with Python Nested List Comprehension, equivalent to the nested for loops, but more succinct

# cast into NumPy array using np.array()

C = np.array([[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)]
              for A_row in A])

print("Nested List Comprehension")
print(C)

# numpys built in matmul()

C = np.matmul(A, B)

print("Numpys matmul()")
print(C)

# or even numpys @-operator works


C = A @ B

print("Numpys @-operator")
print(C)
