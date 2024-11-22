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

    C = A.mul(B)
    C.print()


if __name__ == "__main__":
    main()
