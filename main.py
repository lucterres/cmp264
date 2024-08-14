# Sprint#2 - Protótipo da(s) visualização(ões)Tarefa
# Nesta etapa, você deverá entregar uma apresentação em slides descrevendo um protótipo  da(s) visualização(ões) planejadas,
#  com eventuais interações. Se houver uma primeira implementação, gravar um video e disponibilizar em Google Drive, One Drive ou YouTube. 
# Esta apresentação deverá ser uma evolução da anterior, contendo os progressos realizados desde a etapa inicial. 


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

def load_data(velans):
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


if __name__ == "__main__":
    velans = []

    print ("Program Init")

    load_data(velans)
    for v in velans:
        v.show()


    
    