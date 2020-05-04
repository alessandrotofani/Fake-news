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
        
        ## parte riguardante la trasmissione delle news
        ## lista che contiene l'id delle news ricevute dal vicino
        ## id news = posizione della news nella lista news score
        ## gli id iniziano da 0 per non creare confusione con gli indici
        self.news_ricevute = [] 
        ## lista che contiene l'd news che l'agente ha integrato, cioè i suoi belief 
        self.news_integrate = []
        
        
        
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
        

    ## implemento il preferential attachment per tutti i nodi non collegati 
    def PA(self):
        ## escludo i nodi iniziali che già ho connesso 
        print("Node ", self.number," Creating link with preferential attachment ")
        if self.number > (common.links_per_node + 1):
            link_formed = 0
            my_neighbors = []
            while link_formed < common.links_per_node:
                ## scelgo il nodo a cui connettermi in modo random 
                i = random.choice(common.connectednodes)
                tot = totaldegree()
                ## calcolo la probabilità di connettermi al nodo scelto
                ## probabilità = grado del nodo scelto / grado totale 
                common.prob =  common.g.degree[i] / tot
                if random.random() < common.prob and i not in my_neighbors:
                    ## creo il link tra i duenodi 
                    gvf.createEdge(self, i)
                    common.connectednodes.append(i)
                    my_neighbors.append(i)
                    link_formed += 1
            common.connectednodes.append(self)
        common.PA_done = True 
        return      
    
    ## funzione che crea la news 
    def create_news(self):
        random.seed()
        if self.number == common.news_creator:
            ## assegno lo score della notizia in base allo score dell'agente 
            score = self.score
            ## aggiungo lo score alla lista degli score 
            common.news_score.append(score)
            print("Agent ", self.number," creating news ",common.new_news_id," with score ", score)
        
            for i in common.g.neighbors(self):
                print("Sending news to  ", i.number)
                ## aggiungo l'id della news alla lista delle news ricevute del mio vicino 
                i.news_ricevute.append(common.new_news_id)
        
            common.new_news_id += 1 
        
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
