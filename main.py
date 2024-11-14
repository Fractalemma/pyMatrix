from matrix import Matrix

def main():
    print("Welcome, this program computes the cross product of two given matrices")

    print("\n\n------------------------------ MATRIX A:")
    A = Matrix()
    A.read()
    A.print()

    print("\n\n------------------------------ MATRIX B:")
    B = Matrix()
    B.read()
    B.print()

    

    if A.c == B.r:
        C = Matrix()
        for i in range(A.r):
            C.matrix.append(list([0] * B.c))

        for i in range(A.r):
            for j in range(B.c):
                for k in range(A.c):
                    C.matrix[i][j] += A.matrix[i][k] * B.matrix[k][j]

        """for i in range(r1):
            for j in range(c2):
                C[i][j] += A[i][j]*B[j][i]"""

        print("-------------------------------------------------")
        print(f"The resultant matrix is:")
        for i in range(A.r):
            for j in range(B.c):
                print(f"{C[i][j]}\t", end="")
            print()

    else:
        print("The given matrices cannot be multiplied!")
        print(f"Matrix A has {A.c} columns and Matrix B has {B.r} rows")


if __name__ == "__main__":
    main()
