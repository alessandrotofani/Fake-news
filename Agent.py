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
        # ## assegno lo score a ciuscun agente in modo random 
        self.score = random.random()

        ## creo gli user in proporzione
        ## problema di self.number con i bot
        ## fake news bots
        if self.number <= (10000 + common.number_of_bots * 0.75 ) and self.agType == "bots":
            self.score = random.uniform(0, 0.1)
        ## bias left bots
        if self.number > (10000 + common.number_of_bots * 0.75 ) and self.number <= (10000 + common.number_of_bots) and self.agType == "bots":
            self.score = random.uniform(0.8, 0.9)
        ##fake news users
        if self.number < (0.02 * common.number_of_users):
            self.score = random.uniform(0, 0.1)            
        ## bias right
        if self.number < (0.9 * common.number_of_users) and self.number > (0.02 * common.number_of_users):
            self.score = random.uniform(0.1, 0.2)            
        ## right 
        if self.number < (0.19 * common.number_of_users) and self.number > (0.9 * common.number_of_users):
            self.score = random.uniform(0.2, 0.3)          
        ## right leaning 
        if self.number < (0.25 * common.number_of_users) and self.number > (0.19 * common.number_of_users):
            self.score = random.uniform(0.3, 0.45) 
        ## center
        if self.number < (0.49 * common.number_of_users) and self.number > (0.25 * common.number_of_users):
            self.score = random.uniform(0.45, 0.55) 
        ## left leaning
        if self.number < (0.79 * common.number_of_users) and self.number > (0.49 * common.number_of_users):
            self.score = random.uniform(0.55, 0.7) 
        ## left 
        if self.number < (0.95 * common.number_of_users) and self.number > (0.79 * common.number_of_users):
            self.score = random.uniform(0.7, 0.8) 
        ## bias left 
        if self.number <= common.number_of_users and self.number > (0.95 * common.number_of_users):
            self.score = random.uniform(0.8, 0.9) 
        ## left fake news does not exist
        ## fermo lo score a 0,9 su 1 
        
        
        ## i primi due agenti, che saranno quelli con grado più alto ( causa della costruzione della rete
        ## con il preferential attachment), gli do uno score fisso
        if self.number == 1:
            self.score = 0.80
        if self.number == 2:
            self.score = 0.20
      
        xPos = 0
        yPos = 0
        self.xPos = xPos
        self.yPos = yPos
        
        ## parte riguardante la trasmissione delle news
        ## lista che contiene l'id delle news ricevute dal vicino
        ## id news = posizione della news nella lista news score
        ## gli id iniziano da 0 per non creare confusione con gli indici
        self.news_ricevute = [] 
        ## lista che contiene gli id delle news che devo integrare
        self.news_da_integrare = []
        ## contatore che mi dice fino a dove sono arrivato ad integrare le news
        self.counter_news_ricevute = 0
        ## lista che contiene l'd news che l'agente ha integrato, cioè i suoi belief 
        self.news_integrate = []
        
        
        
        # the graph
        if gvf.getGraph() == 0:
            gvf.createGraph()

        # the agent
        ## stampo l'agente che ho creato
        print("agent of type", self.agType,
              "#", self.number, "has been with score ", self.score)
            
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
        # print("Node ", self.number," Creating link with preferential attachment ")
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
                    ## creo il link tra i due nodi 
                    # gvf.createEdge(self, i)
                    gvf.createEdge(i, self)
                    common.connectednodes.append(i)
                    my_neighbors.append(i)
                    link_formed += 1
            common.connectednodes.append(self)
        common.PA_done = True 
        return      
    
        
    ## funzione che crea la news 
    def create_news(self):
        random.seed()
        # common.news_creator = random.randint(1, common.total_number_of_nodes)
        if self.number == common.news_creator:
            ## assegno lo score della notizia in base allo score dell'agente 
            score = self.score
            ## aggiungo le feature della news al dizionario che contiene tutte le news 
            common.news.append({"id" : common.new_news_id , 
                                "autore" : self,
                                "score" : self.score,
                                "id autore" : self.number,
                                "agent type" : self.agType})    
            print("Agent ", self.number," creating news ",common.new_news_id," with score ", score)
            
            send_news(self, common.new_news_id)
            common.new_news_id += 1 
        
        return
     
    ## funzione che permette ai bot di creare la news 
    ## non c'è un controllo sill'id dei bot quando creo la news
    ## circa il 4% degli utenti sono bot
    ## generano più tweet dei normali user 
    ## interazione human-human come quella bot-human     
    def bot_create_news(self):
        random.seed()
        score = random.uniform(0, 0.1)
        ## aggiungo le feature della news al dizionario che contiene tutte le news 
        common.news.append({"id" : common.new_news_id , 
                            "autore" : self,
                            "score" : self.score,
                            "id autore" : self.number,
                            "agent type" : self.agType})    
        print("Agent ", self.number," creating news ",common.new_news_id," with score ", score)
        
        send_news(self, common.new_news_id)
        common.new_news_id += 1
        
        
        return
    
        
    
    ## funzione per integrare la news che mi arriva 
    ## https://www.geeksforgeeks.org/python-find-dictionary-matching-value-in-list/
    def integrate_news(self):
        random.seed()
        # provo a integrare le news che mi sono appena arrivate
        for i in self.news_da_integrare:
            ## seleziono la news dal dictionary che le contiene tutte 
            for news in common.news:
                if news["id"] == i:
                    ## estraggo le feature della news 
                    news_score = news["score"]
                    autore = news["autore"]
                    ## https://stackoverflow.com/questions/10406130/check-if-something-is-not-in-a-list-in-python
                    ## controllo che io non sia l'autore della news
                    ## controllo che non abbia già ricondiviso la news 
                    if autore != self and i not in self.news_integrate:
                        ## le integro se lo score della news è abbastanza vicino al mio score 
                        if abs(self.score - news_score) < random.random():
                            print("News ", i, " with score ", news_score," tweeted by ", 
                                  autore.number," has been retweeted by agent ", self.number  )
                            ## aggiungo l'id della news tra le news integrate
                            self.news_integrate.append(i)
                            ## se integro la news allora modifico il mio score a seconda 
                            # ## dello score della news integrata 
                            # self.score = self.score + ((news_score - 0.5) / 100 )
                            ## mando la notizia ai miei follower
                            send_news(self, i)
                            ## creo un link con l'autore della news
                            # gvf.createEdge(self, autore)
                            gvf.createEdge(autore, self)
                            ## aumento il contatore delle news ricevute 
                            self.counter_news_ricevute += 1
        ## pulisco la lista delle news da integrare 
        del self.news_da_integrare[:]        
        return   
    
    ## funzione per integrare la news che arriva al bot
    ## https://www.geeksforgeeks.org/python-find-dictionary-matching-value-in-list/
    def bot_integrate_news(self):
        random.seed()
        # provo a integrare le news che mi sono appena arrivate
        for i in self.news_da_integrare:
            ## seleziono la news dal dictionary che le contiene tutte 
            for news in common.news:
                if news["id"] == i:
                    ## estraggo le feature della news 
                    news_score = news["score"]
                    autore = news["autore"]
                    ## https://stackoverflow.com/questions/10406130/check-if-something-is-not-in-a-list-in-python
                    ## controllo che io non sia l'autore della news
                    ## controllo che non abbia già ricondiviso la news 
                    if autore != self and i not in self.news_integrate:
                        ## le integro se lo score della news è abbastanza vicino al mio score 
                        if news_score <= 0.1:
                            print("News ", i, " with score ", news_score," tweeted by ", 
                                  autore.number," has been retweeted by agent ", self.number  )
                            ## aggiungo l'id della news tra le news integrate
                            self.news_integrate.append(i)
                            ## se integro la news allora modifico il mio score a seconda 
                            # ## dello score della news integrata 
                            # self.score = self.score + ((news_score - 0.5) / 100 )
                            ## mando la notizia ai miei follower
                            send_news(self, i)
                            ## creo un link con l'autore della news
                            # gvf.createEdge(self, autore)
                            gvf.createEdge(autore, self)
                            ## aumento il contatore delle news ricevute 
                            self.counter_news_ricevute += 1
        ## pulisco la lista delle news da integrare 
        del self.news_da_integrare[:]        
        return   
    
    
    
    
## calcola la somma dei degree di tutti i nodi 
def totaldegree(): ## funziona 
    totaldegree = 0
    for i in common.orderedListOfNodes:
        totaldegree += common.g.degree[i]   
    return totaldegree  


## funzione che serve per inviare la news 
def send_news(self, news_to_send):
    done = False ## serve per controllare se il nodo ha dei predecessors o no 
    try:
        ## seleziono i destinatari della news =  i miei follower 
        # for i in common.g.predecessors(self):
        for i in common.g.neighbors(self):
            print("Sending news to  ", i.number)
            ## aggiungo l'id della news alla lista delle news ricevute del mio follower
            i.news_ricevute.append(news_to_send)   
            ## aggiungo l'id della news alla lista delle news da integrare del mio follower
            i.news_da_integrare.append(news_to_send)   
            done = True 
            
        ## se il nodo selezionato non ha follower, allora sceglie un nodo a caso e la manda a lui        
        if not done:
            i = random.choice(common.orderedListOfNodes)
            print("Sending news to  ", i.number)
            ## aggiungo l'id della news alla lista delle news ricevute dal destinatario
            i.news_ricevute.append(news_to_send)
            ## aggiungo l'id della news alla lista delle news da integrare del mio follower
            i.news_da_integrare.append(news_to_send)
                   
    except BaseException:
        print("Not done")        
     
    return



def modPosition():
    if random.randint(0, 1) == 0:
        return random.randint(-8, -6)
    else:
        return random.randint(6, 8)