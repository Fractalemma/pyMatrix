from matrix import Matrix

def main():
    print("Welcome, this program computes the cross product of two given matrices")

    print("\n\n------------------------------ MATRIX A:")
    A = Matrix()
    A.read()
    A.print()

    if c1 == r2:
        C = []
        for i in range(r1):
            C.append(list([0] * c2))

        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    C[i][j] += A[i][k] * B[k][j]

        """for i in range(r1):
            for j in range(c2):
                C[i][j] += A[i][j]*B[j][i]"""

        print("-------------------------------------------------")
        print(f"The resultant matrix is:")
        for i in range(r1):
            for j in range(c2):
                print(f"{C[i][j]}\t", end="")
            print()

    else:
        print("The given matrices cannot be multiplied!")
        print(f"Matrix A has {c1} columns and Matrix B has {r2} rows")


if __name__ == "__main__":
    main()
