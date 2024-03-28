import random
from abc import abstractmethod
from abc import ABC

class Element:
    '''
    klasa Element, koja se sastoji samo od liste brojeva koji predstavljaju element koji treba dodati u listu
    '''
    def __init__(self, list):
        self.size = len(list)
        self.elelist = list
    
    def getSize(self):
        return self.size
    
    def getList(self):
        return self.elelist
    
class Alokator:
    '''
    klasa Alokator, prosledjuje joj se broj elemenata liste koja predstavlja memoriju, kao i string u kom se govori koji algoritam treba da se primeni
    '''
    def __init__(self, n, algorithm):
        #bilo al pa l pa lista
        self.allocated_list = [random.randint(0, 1) for _ in range (n)] #formiranje liste koja je memorija, gde 1 predstavlja mesto koje je zauzeto, formira se random od 0 i 1
        self.memory_list = [0] * n #iste je duzine kao prethodna lista, i za svaki deo memorije pokazuje sta se tu nalazi, na pocetku je formirana samo od 0 pa se posle dodaju elementi
        self.algorithm = algorithm
        self.positions_list = []
    
    def getElement(self, ind):
        poc = self.positions_list[ind][0]
        kraj = self.positions_list[ind][0] + self.positions_list[ind][1]
        return self.memory_list[poc:kraj]
    
    def algoritam(self, ele): #poziva odredjeni algoritam u zavisnosti od informacije poslate stringom
        if self.algorithm == "FirstFit":
            #return FirstFit.find(ele, self.al, self.l, self.lista) #poziva FirstFit ako je to trazeno
            return FirstFit.find(ele, self.allocated_list, self.memory_list, self.positions_list)
        elif self.algorithm == "BestFit":
            #return BestFit.find(ele, self.al, self.l, self.lista) #poziva BestFit ako je to trazeno
            return BestFit.find(ele, self.allocated_list, self.memory_list, self.positions_list)
        else:
            return None, None #vraca None, None jer i ove dve funkcije vracaju dva argumenta, a posle u mainu proverava ako je none none pa ispisuje gresku

class Algoritam(ABC): 
    '''
    klasa algoritam u kojoj se nalazi abstraktna metoda find koja se implementira u okviru FirstFind i BestFind klasa
    '''
    def __init__(self):
        None

    @abstractmethod
    def find(ele, l, l2): #abstraktna metoda find
        ...

class FirstFit(Algoritam): 
    '''
    klasa FirstFit, dete klase Algoritam
    '''
    def __init__(self):
        super().__init__()

    def find(ele, l, l2, lista): #implementira FirstFit algoritam u okviru funkcije find
        eleSize = ele.getSize() #koliko polja zauzima element
        blockSize = 0 #brojimo u ovoj promenljivoj prazna polja u listi koja predstavlja memoriju
        eleList = ele.getList() #lista koja predstavlja ono za sta treba da alociramo mesto u memoriji
        k = 0
        for i in range(len(l)): 
            if l[i] == 0:
                blockSize += 1
            else:
                blockSize = 0
        
            if blockSize >= eleSize: 
                for j in range(eleSize):
                    l2[j + i - eleSize + 1] = eleList[j]
                    l[j + i - eleSize + 1] = 1
                lista.append((i - eleSize + 1, eleSize))
                k = 1
                return i - eleSize + 1, l2
                
        if k == 0:
            return -1, l2 #vraca -1 za poziciju ako nije uspeo da nadje mesto tj ako nema mesta u memoriji kako bi kasnije identifikovali gresku
            
class BestFit(Algoritam): 
    '''
    klasa FirstFit, dete klase Algoritam
    '''
    def __init__(self):
        super().__init__()

    def find(ele, l, l2, lista): #implementira FirstFit algoritam u okviru funkcije find
        eleSize = ele.getSize() #koliko polja zauzima element
        blockSize = 0 #brojimo u ovoj promenljivoj prazna polja u listi koja predstavlja memoriju
        mini = 500 #stavili smo veliki broj kao minimalno mesta a da je vece od duzine elementa, broj moze da se menja po potrebi (u slucaju ako imamo listu gde je 500 blokova ili vise stvarno najbolja opcija za pakovanje elementa)
        ind = -1 #indeks stavljamo na -1 da bi u slucaju da ne nadje memoriju znali da je nije nasao i kako bismo kasnije identifikovali gresku
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
        lista.append((ind + 1, eleSize))
        return  ind + 1, l2

brojevi = list(map(int, input().split()))
e = Element(brojevi)
n = int(input())
fit = str(input())

a = Alokator(n, fit)
print(a.allocated_list)
print(a.memory_list)
print("-------------------------")


if len(e.getList()) > n:
    print("Error: nema mesta u memoriji za element, veci je od cele memorije")
else:
    prvo, drugo = a.algoritam(e)
    if prvo == drugo == None:
        print("Error: ovaj algoritam ne postoji")   
    elif prvo == -1:
        print("Error: u memoriji nema mesta da se ubaci ovaj element")
    else:
        print(prvo)
        print(drugo)
        print("-------------------------")
        print(a.allocated_list)

print(a.getElement(0))







