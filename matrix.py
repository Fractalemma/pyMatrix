class Matrix:
    # r = 0
    def __init__(self):
        self.matrix = []
        self.r = 0
        self.c = 0

    def read(self):
        self.r = int(input("Please enter the number of rows of the matrix: "))
        self.c = int(input("Please enter the number of columns of the matrix: "))

        self.matrix = []
        for i in range(self.r):
            self.matrix.append(list([0] * self.c))

        for i in range(self.r):
            for j in range(self.c):
                print(f"M[{i},{j}] = ", end="")
                self.matrix[i][j] = int(input())

    def print(self):
        # print(f"The given matrix is:")
        for i in range(self.r):
            for j in range(self.c):
                print(f"{self.matrix[i][j]}\t", end="")
            print()

    def mul(self, B):
        if self.c == B.r:
            C = Matrix()
            C.r = self.r
            C.c = B.c
            for i in range(self.r):
                C.matrix.append(list([0] * B.c))

            for i in range(self.r):
                for j in range(B.c):
                    for k in range(self.c):
                        C.matrix[i][j] += self.matrix[i][k] * B.matrix[k][j]
            return C
        else:
            raise Exception("Illegal operation: incompatible dimensions")

    def scalar(self, k):
        R = Matrix()
        R.r = self.r
        R.c = self.c

        for i in range(self.r):
            R.matrix.append(list([0] * self.c))

        for i in range(self.r):
            for j in range(self.c):
                R.matrix[i][j] = self.matrix[i][j] * k

        return R

    def det(self):
        matrix = self.matrix
        return (
            matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
            - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
            + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
        )

    def adj(self):
        matrix = self.matrix
        adj = [[0, 0, 0] for _ in range(3)]

        adj[0][0] = matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]
        adj[0][1] = -(matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        adj[0][2] = matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]

        adj[1][0] = -(matrix[0][1] * matrix[2][2] - matrix[0][2] * matrix[2][1])
        adj[1][1] = matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]
        adj[1][2] = -(matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0])

        adj[2][0] = matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]
        adj[2][1] = -(matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0])
        adj[2][2] = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        return adj

    def inv(self):
        matrix = self.matrix
        det = self.det()

        # Si el determinante es 0, la matrix no tiene inversa
        if det == 0:
            print("La matrix no tiene inversa (determinante = 0).")
            return None

        # Calcular la adjunta
        adj = self.adj()

        # Calcular la inversa (adjunta / determinante)
        inversa_matrix = [[adj[i][j] / det for j in range(3)] for i in range(3)]
        return inversa_matrix
