class Matrix:
    #r = 0
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
        print(f"The given matrix is:")
        for i in range(self.r):
            for j in range(self.c):
                print(f"{self.matrix[i][j]}\t", end="")
            print()

    def mul(self, B):
        if self.c == B.r:
            C = Matrix()
            for i in range(self.r):
                C.matrix.append(list([0] * B.c))

            for i in range(self.r):
                for j in range(B.c):
                    for k in range(self.c):
                        C.matrix[i][j] += self.matrix[i][k] * B.matrix[k][j]
            return C
        raise Exception("Something is wrong")
                        
        