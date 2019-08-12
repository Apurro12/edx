import matplotlib.pyplot as plt

#Visualizacion de la dinamica del ecosistema
plt.axis([-1,1,-1,1])
plt.ion()

for i in range(10):
    plt.axis([-1,1,-1,1])
    plt.scatter([i,i],[1,1], c='r')
    plt.scatter([1,1],[i,i], c='b')
    plt.savefig(str(i)+'.png', dpi=100)
    plt.pause(0.2)
    plt.cla()