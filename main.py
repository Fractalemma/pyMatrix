import os
os.system('cls')

print("Welcome, this program computes the cross product of two given matrices")

print("\n\n------------------------------ MATRIX A:")
r1 = int(input("Please enter the number of rows of the first matrix: "))
c1 = int(input("Please enter the number of columns of the first matrix: "))

A = []
for i in range(r1):
    A.append(list([0]*c1))

for i in range(r1):
    for j in range(c1):
        print(f'A[{i},{j}] = ',end='')
        A[i][j] = int(input())

print(f'The given matrix is:')
for i in range(r1):
    for j in range(c1):
        print(f'{A[i][j]}\t',end='')
    print()

print("------------------------------ MATRIX B:")
r2 = int(input("Please enter the number of rows of the second matrix: "))
c2 = int(input("Please enter the number of columns of the second matrix: "))

B = []
for i in range(r2):
    B.append(list([0]*c2))

for i in range(r2):
    for j in range(c2):
        print(f'B[{i},{j}] = ',end='')
        B[i][j] = int(input())

print(f'The given matrix is:')
for i in range(r2):
    for j in range(c2):
        print(f'{B[i][j]}\t',end='')
    print()


if (c1 == r2):
    C = []
    for i in range(r1):
        C.append(list([0]*c2))

    for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    C[i][j] += A[i][k] * B[k][j]

    '''for i in range(r1):
        for j in range(c2):
            C[i][j] += A[i][j]*B[j][i]'''

    print("-------------------------------------------------")
    print(f'The resultant matrix is:')
    for i in range(r1):
        for j in range(c2):
            print(f'{C[i][j]}\t',end='')
        print()

else:
    print("The given matrices cannot be multiplied!")
    print(f"Matrix A has {c1} columns and Matrix B has {r2} rows")