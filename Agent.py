from Tools import *
from agTools import *
import graphicDisplayGlobalVarAndFunctions as gvf
import commonVar as common
import random 


## definisco l'agente e tutti i metodi
class Agent(SuperAgent):
    
    ## definisco il costruttore 
    ## ricorda che le variabili x = valore, vanno messe alla fine 
    def __init__(self, number, myWorldState,
                 xPos=0, yPos=0, lX=0, rX=0, bY=0, tY=0, agType="",
                 ):
        
        # the environment
        self.agOperatingSets = []
        ## ricorda che self.number parte da 1
        ## invece l'indice de orderedListOfNodes parte da 0 
        self.number = number
        ## metto il nodo appena creato nella lista che li contiene tutti
        ## nota: quando si passa self, si passa l'intero oggetto, quando invece si passa self.parametro,
        ## si passa solo il valore di quel parametro 
        common.orderedListOfNodes.append(self)
        self.myWorldState = myWorldState
        self.agType = agType
        ## assegno lo score a ciuscun agente in modo random 
        self.score = random.random()
        ## i primi due agenti, che saranno quelli con grado più alto ( causa della costruzione della rete
        ## con il preferential attachment), gli do uno score fisso
        if self.number == 1:
            self.score = 0.80
        if self.number == 2:
            self.score = 0.20           
        xPos = random.uniform(-9, 9)
        yPos = random.uniform(-9, 9)
        self.xPos = xPos
        self.yPos = yPos
        
        
        # the graph
        if gvf.getGraph() == 0:
            gvf.createGraph()

        # the agent
        ## stampo l'agente che ho creato
        print("agent of type", self.agType,
              "#", self.number, "has been created at", self.xPos, ",", self.yPos, " with score ", self.score)
            
        ## aggiungo un nodo, corrispondente all'agente creato, nel grafo 
        common.g.add_node(self)
        gvf.colors[self] = "LightGray"
        gvf.pos[self] = (xPos, yPos)
        gvf.pos[self.number] = (xPos, yPos)
        common.g_labels[self] = str(number)


    def getGraph(self):
        return common.g

    ## funzione usata per inizializzare il preferential attachment
    ## devo creare un sottografo connesso di m nodi, con m =< links_per_node
    def initializePA(self): 
        ## ricorda che self.number parte da 1
        ## invece l'indice de orderedListOfNodes parte da 0 
        if self.number < (common.links_per_node + 2) :
            i = 1
            while i < (common.links_per_node + 2):             
                if i != (self.number):
                    print("self number ", self.number," i ", i)
                    gvf.createEdge(self,common.orderedListOfNodes[i-1])
                    ## aggiungo ilnodo che si è connesso alla lista che contiene
                    ## tutti i nodi già connessi
                    ## fare ciò è utile per velocizzare l'algortimo di preferential attachment 
                    common.connectednodes.append(self)
                i += 1
        random.seed()
        return

    ## implemento il preferential attachment per tutti i nodi non collegati 
    def PA(self):
        ## escludo i nodi iniziali che già ho connesso 
        if self.number > 2:
            link_formed = 0
            while link_formed < common.links_per_node:
                ## scelgo il nodo a cui connettermi in modo random 
                i = random.choice(common.connectednodes)
                tot = totaldegree()
                ## calcolo la probabilità di connettermi al nodo scelto
                ## probabilità = grado del nodo scelto / grado totale 
                common.prob =  common.g.degree[i] / tot
                if random.random() < common.prob:
                    ## creo il link tra i duenodi 
                    gvf.createEdge(self, i)
                    common.connectednodes.append(i)
                    link_formed += 1
            common.connectednodes.append(self)
        common.PA_done = True 
        return      
    
## calcola la somma dei degree di tutti i nodi 
def totaldegree(): ## funziona 
    totaldegree = 0
    for i in common.orderedListOfNodes:
        totaldegree += common.g.degree[i]   
    return totaldegree  


def modPosition():
    if random.randint(0, 1) == 0:
        return random.randint(-8, -6)
    else:
        return random.randint(6, 8)
