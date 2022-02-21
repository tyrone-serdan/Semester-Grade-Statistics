from cProfile import label
import matplotlib.pyplot as plt

def showData(x,y, barNames):
    plt.bar(x,y)
    addlabels(x,y)
    
    plt.ylabel('Weight')
    plt.xlabel('Data')
    plt.title("Percentile Ranks")
    
    plt.xticks(ticks=x, labels=barNames)
    
    plt.show()
    
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i + 1, y[i], str(y[i]) + '%', ha='center')
