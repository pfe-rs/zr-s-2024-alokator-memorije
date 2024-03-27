import random

class Element:
    def __init__(self, list):
        self.size = len(list)
        self.elelist = list
    
    def getSize(self):
        return self.size
    
    def getList(self):
        return self.elelist
    
class Alokator:
    def __init__(self, n, algorithm):
        self.al = [random.randint(0, 1) for _ in range (10)]
        self.l = [0] * n
        self.algorithm = algorithm

    def getAllocatedList(self):
        return self.al

    def getList(self):
        return self.l
    
    def algoritam(self, ele):
        if self.algorithm == "FirstFit":
            return Algoritam.firstFit(ele, self.al, self.l)
        elif self.algorithm == "BestFit":
            return Algoritam.bestFit(ele, self.al, self.l)
        else:
            return "Ovaj algoritam ne postoji"

class Algoritam:
    def __init__(self):
        None

    @staticmethod
    def firstFit(ele, l, l2):
        eleSize = ele.getSize()
        blockSize = 0
        eleList = ele.getList()
        for i in range(len(l)): 
            if l[i] == 0:
                blockSize += 1
            else:
                blockSize = 0
        
            if blockSize >= eleSize: 
                for j in range(eleSize):
                    l2[j + i - eleSize + 1] = eleList[j]
                    l[j + i - eleSize + 1] = 1
                return i - eleSize + 1, l2

    @staticmethod
    def bestFit(ele, l, l2):
        eleSize = ele.getSize()
        blockSize = 0
        mini = 500
        ind = 0
        eleList = ele.getList()
        for i in range(len(l) - 1): 
            if l[i] == 0:
                blockSize += 1
            else:
                blockSize = 0
        
            if blockSize >= eleSize and l[i + 1] == 1 and blockSize < mini: 
                mini = blockSize
                ind = i - blockSize
        
        if l[i + 1] == 0:
            blockSize += 1
            if blockSize >= eleSize and blockSize < mini: 
                mini = blockSize
                ind = i - blockSize
        
        for j in range(eleSize):
            l2[j + ind + 1] = eleList[j]
            l[j + ind + 1] = 1
        return  ind + 1, l2

brojevi = list(map(int, input().split()))
e = Element(brojevi)
n = int(input())
fit = input()
a = Alokator(n, fit)
print(a.getAllocatedList())
print(a.getList())
print("-------------------------")

prvo, drugo = a.algoritam(e)

print(prvo)
print(drugo)
print("-------------------------")
print(a.getAllocatedList())