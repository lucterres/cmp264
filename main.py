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
        print(self.coordX , self.coordY)
        print ('z   ', '  veloc')
        for i in range(len(self.zlist)):
            print(self.zlist[i], self.velocitylist[i])
    