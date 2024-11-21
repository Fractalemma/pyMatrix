class Matrix:
    matrix=[] 

    def __init__(self):
        self.matrix=[]

    def read(self):
        rows = 2
        colums = 2
        self.matrix = []

        # Primera Matriz 
        print("Agrega los valores de la matriz")
        for i in range (rows):
            fila = []
            for j in range (colums):
                val = input()
                fila.append(val)
            self.matrix.append(fila)

    def print(self):
        print("Tu matriz 1 es")
        for fila in self.matrix: 
            print(fila)

    def mul(self):
        pass