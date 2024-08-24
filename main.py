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
        x = np.linspace(xMin, xMax, ix)
        y = np.linspace(yMin, yMax, jy)
        self.X, self.Y = np.meshgrid(x, y)
        # Crie os dados para o eixo Z
        self.Z = np.zeros((jy, ix))
    def getGrid(self):
        return self.X, self.Y, self.Z

# 341920359
#VELF                 1033 2280 1350 2408 1657 2518 2273 2714 4048 3192
#VELF                 1605 2485 1809 2551 2825 2857 4518 333710216 4248 
#SPNT       6147       163 1188797.5 7598759.6   0530415  
#01234567890123456789012345678901234567890123456789012345678901234567890
#0         1         2         3         4         5         6         7
#                     1    6    1    6    1    6    1    6    1    6       
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
    filename = "data/velans1.txt"
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

def loadGrd(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        tokens = lines[1].split()
        ix = int(tokens[0])
        jy = int(tokens[1])
        
        tokens = lines[2].split()
        xMin = int(tokens[0])
        xMax = int(tokens[1])
        
        tokens = lines[3].split()
        yMin = int(tokens[0])
        yMax = int(tokens[1])
        
        tokens = lines[4].split()
        zMin = float(tokens[0])
        zMax = float(tokens[1])

        Z = np.zeros((jy, ix))

        for j in range(jy):
            line=lines[j+5]
            tokens = line.split()
            for i in range(ix):
                z = tokens[i]
                if z == "999999":
                     Z[j,i] = np.nan
                else:
                     Z[j,i] = float(z)

    map = Grid(ix, jy, xMin, xMax, yMin, yMax, zMin, zMax)
    map.Z = Z
      
    return map

def show2D(map,title="", scalecolorLabel="",cmap='viridis'):

    X, Y, Z = map.getGrid()
    # Crie um scatter plot com a escala de cores definida por z
    plt.scatter(X, Y, c=Z, cmap=cmap)
    # Adicione uma barra de cores
    plt.colorbar(label=scalecolorLabel)
    # Adicione um título
    plt.title(title)
    # Mostre o gráfico
    plt.show()

def show3D(map,title=""):
    X, Y, Z = map.getGrid()

    # Crie uma figura
    fig = plt.figure(figsize=(10, 10))
    plt.title(title)

    # Adicione um gráfico 3D à figura
    ax = fig.add_subplot(111, projection='3d')
    
    # Plote a superfície
    # Plote a superfície com uma única cor
    #ax.plot_surface(X, Y, Z, color='gray')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    # Plote a superfície com a escala de cores definida por outra variável
    #ax.plot_surface(X, Y, Z, cmap='viridis', facecolors=colors, rstride=1, cstride=1, linewidth=0, antialiased=False)

    
    # Adjust the vertical exaggeration by setting z-axis limits
    z_min, z_max = map.zMin, map.zMax
    ax.set_zlim(z_min, z_max / 40)  # Adjust the divisor to control exaggeration

    # Mostre o gráfico
    plt.show()

def colorProjection3D(surface, geopressure, legend="",cmap='viridis',title=""):
    # Supondo que X, Y, Z e D já estejam definidos
    X,Y,Z = surface.getGrid()
    D = geopressure.Z

    # Normalizar D para o intervalo [0, 1]
    norm = plt.Normalize(geopressure.zMin, geopressure.zMax)
    
    if cmap == 'viridis':
        colors = plt.cm.viridis(norm(D))
    else:
        colors = plt.cm.Reds(norm(D))

    # Criar a figura
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title(title)
    
    # Adjust the vertical exaggeration by setting z-axis limits
    z_min, z_max = surface.zMin, surface.zMax
    ax.set_zlim(z_min, z_max / 40)  # Adjust the divisor to control exaggeration

    # Plotar a superfície com a escala de cores definida por D
    surf = ax.plot_surface(X, Y, Z, facecolors=colors, rstride=1, cstride=1, linewidth=0, antialiased=False)

    # Mostrar a barra de cores
    mappable = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    mappable.set_array(D)
    plt.colorbar(mappable, ax=ax, label=legend)

    # Mostrar o gráfico
    plt.show()
    
if __name__ == "__main__":
    velans = []

    print ("Program Init")
    #loadVelandata(velans)
    #for v in velans:
    #    v.show()



    # Fundo do Mar
    fundomar = r"data\depth\0Ma_Fundo_Mar_Prof.grd"
    densityFundo = r"data\density/000_density.grd"
    surfaceFundomar = loadGrd(fundomar)
    densityFundo = loadGrd(densityFundo)
    show2D(surfaceFundomar,title="Mapa de Profundidade do Fundo do Mar", scalecolorLabel="Profundidade")
    show3D(surfaceFundomar,title="Superfície 3D para Fundo do Mar - Profundidade")
    show2D(densityFundo,title="Densidade no Fundo do Mar", scalecolorLabel="Densidade g/cm3",cmap='viridis')
    colorProjection3D(surfaceFundomar, densityFundo, 
                      legend="Densidade g/cm3",
                      cmap='viridis',
                      title="Densidade no Fundo do Mar ")
    
    # 023 Oligoceno
    superfic = "Oligoceno"
    depthMap = r"data\depth\23Ma_Oligoceno_Indiviso.grd"
    denisityMap = r"data\density/023_density.grd"
    surface = loadGrd(depthMap)
    density = loadGrd(denisityMap)
    show2D(surface,title="Mapa de Profundidade do " + superfic, scalecolorLabel="Profundidade")
    show3D(surface,title="Superfície 3D para  " + superfic + " - Profundidade")
    show2D(density,title="Densidade no " + superfic, scalecolorLabel="Densidade g/cm3",cmap='viridis')
    colorProjection3D(surface, density, 
                      legend="Densidade g/cm3",
                      cmap='viridis',
                      title="Densidade no  " + superfic)

    # Superfície Topo do Sal
    topoSal = r"data\depth\112Ma_Topo_Sal.grd"
    filegeopressure112= r"data\geopressure\Event_pressure_on_112age.grd"
    surface = loadGrd(topoSal)
    pressure = loadGrd(filegeopressure112)
    show2D(surface,title="Mapa de Profundidade da Superfície Topo do Sal ", scalecolorLabel="Profundidade")
    show3D(surface,title="Superfície 3D para Topo do Sal - Profundidade")  
    colorProjection3D(surface, surface, 
                      legend="Profundidade",
                      cmap='viridis',
                      title="Superfície 3D para Topo do Sal ")

    # Mapa de Pressão Geostática
    show2D(pressure,
           title="Geopressão na camada Topo do Sal", 
           scalecolorLabel="Pressão",
           cmap='Reds')
    
    # Mostrar a projeção colorida em 3D
    colorProjection3D(surface, pressure, "Pressão na superfície MPa", cmap='Reds',title="Pressão na superfície 3D")