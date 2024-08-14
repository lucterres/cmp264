# Sprint#2 - Protótipo da(s) visualização(ões)Tarefa
# Nesta etapa, você deverá entregar uma apresentação em slides descrevendo um protótipo  da(s) visualização(ões) planejadas,
#  com eventuais interações. Se houver uma primeira implementação, gravar um video e disponibilizar em Google Drive, One Drive ou YouTube. 
# Esta apresentação deverá ser uma evolução da anterior, contendo os progressos realizados desde a etapa inicial. 

import numpy as np
import matplotlib.pyplot as plt
from itertools import islice


class Grid:
    def __init__(self, ix, jy, xMin, xMax, yMin, yMax,zMin, zMax):
        self.ix = ix
        self.jy = jy
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.zMin = zMin
        self.zMax = zMax
        self.xCellSize = (xMax - xMin) / (ix-1)
        self.yCellSize = (yMax - yMin) / (jy-1)
        # Crie os dados para o eixo X, Y
        self.X = np.linspace(xMin, xMax, ix)
        self.Y = np.linspace(yMin, yMax, jy)
        self.X, self.Y = np.meshgrid(self.X, self.Y)
        # Crie os dados para o eixo Z
        self.Z = np.zeros((ix, jy))
        self.Z[:,:] = zMin
        # Crie os dados para a velocidade


class Velan:
    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY
        #create list of pairs z and velocity
        self.zlist = []
        self.velocitylist = []

    def add(self,z,velocity):
        #add z and velocity to the list
        self.zlist.append(z)
        self.velocitylist.append(velocity)
    def show(self):
        print("Velan x: ", self.coordX , " y:", self.coordY)
        print ('z   ', '  veloc')
        for i in range(len(self.zlist)):
            print(self.zlist[i], self.velocitylist[i])

def loadVelandata(velans):
    # Python
    filename = "velans1.txt"
    # Open the file in read mode ('r')
    with open(filename, 'r') as file:
        # Read the content of the file
        i = 0
        for line in file:
            line = line.rstrip()  # Remove trailing spaces
            lineType = line[0]
            if lineType == "S":
                # extract coordinates;
                coordX, coordY = line[25:35], line[36:45]
                #print(lineType, coordX, coordY)
                # Cria uma instância da classe Velan
                velan_instance = Velan(coordX, coordY)
                #crie uma lista de velans   
                velans.append(velan_instance)
                continue


            if line[0] == "V":
                lineSize = len(line)
                for i in range(20, lineSize, 10):
                    if i + 10 <= lineSize:
                        z, velocity =  line[i:i+5],  line[i+6:i+10]
                        #print(z, velocity)
                        #get the last element of the list velans
                        velan_instance = velans[-1]
                        velan_instance.add(z,velocity)
                        continue
                    
    return velans


def loadGrd():
    # Python
    filename = r"data\depth\65Ma_Topo_Cretaceo.grd"
    # Open the file in read mode ('r')
    with open(filename, 'r') as file:
        lines = file.readlines()
        line=lines[1]
        tokens = line.split()
        ix = int(tokens[0])
        jy = int(tokens[1])
        line=lines[2]
        tokens = line.split()
        xMin = int(tokens[0])
        xMax = int(tokens[1])
        line=lines[3]
        tokens = line.split()
        yMin = int(tokens[0])
        yMax = int(tokens[1])
        line=lines[4]
        tokens = line.split()
        zMin = float(tokens[0])
        zMax = float(tokens[1])
        print(ix, jy, xMin, xMax, yMin, yMax, zMin, zMax)
        x = np.linspace(xMin, xMax, ix)
        y = np.linspace(yMin, yMax, jy)
        X,Y = np.meshgrid(x,y)
        Z = X.copy()
        for j in range(jy):
            line=lines[j+5]
            tokens = line.split()
            for i in range(ix):
                z = tokens[i]
                if z == "999999":
                     Z[j,i] = np.nan
                else:
                     Z[j,i] = float(z)
        print(Z[50,:])

        
    return X,Y,Z

def showFigure(X,Y,Z):
    # Crie uma figura
    fig = plt.figure(figsize=(10, 10))

    # Adicione um gráfico 3D à figura
    ax = fig.add_subplot(111, projection='3d')

    # Plote a superfície
    ax.plot_surface(X, Y, Z, cmap='viridis')

    # Mostre o gráfico
    plt.show()

    
if __name__ == "__main__":
    velans = []

    print ("Program Init")
    loadVelandata(velans)
    for v in velans:
        v.show()
    X,Y,Z = loadGrd()
    showFigure(X,Y,Z)
    
    
    