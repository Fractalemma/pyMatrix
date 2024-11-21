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
        #print(f"The given matrix is:")
        for i in range(self.r):
            for j in range(self.c):
                print(f"{self.matrix[i][j]}\t", end="")
            print()

    def mul(self):
        pass

    def scalar(self,k):
        R = Matrix()
        R.r = self.r
        R.c = self.c

        for i in range(self.r):
            R.matrix.append(list([0] * self.c))
            

        for i in range(self.r):
            for j in range(self.c):
                R.matrix[i][j] = self.matrix[i][j]*k

        return R