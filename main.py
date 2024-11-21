from matrix import Matrix

def main():
    print("Matriz A:")
    A = Matrix()
    A.read()

    print("\nMatriz B:")
    B = Matrix()
    B.read()

    print("\nMatriz A:")
    A.print()

    print("\nMatriz B:")
    B.print()

    print("\nProducto de A y B:")
    try:
        result = A.mul(B)
        for fila in result:
            print(" ".join(map(str, fila)))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
