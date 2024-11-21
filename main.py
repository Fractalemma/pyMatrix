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

    print("The result of mutiplying A and B is:")
    C = Matrix()
    C = A.mul(B)
    C.print()

    print("5.55 times the A matrix equals:")
    S = A.scalar(5.55)
    S.print()


if __name__ == "__main__":
    main()
