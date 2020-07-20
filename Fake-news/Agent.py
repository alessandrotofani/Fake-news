from Tools import *
from agTools import *
import pandas as pd
import graphicDisplayGlobalVarAndFunctions as gvf
import commonVar as common
import random
import math


## definisco l'agente e tutti i metodi
class Agent(SuperAgent):
    
    ## definisco il costruttore 
    ## ricorda che le variabili x = valore, vanno messe alla fine 
    def __init__(self, number, myWorldState,
                 xPos=0, yPos=0, lX=0, rX=0, bY=0, tY=0, agType="",
                 ):
        
        # the environment
        self.agOperatingSets = []
        ## ricorda che self.number parte da 0
        ## invece l'indice de orderedListOfNodes parte da 0 
        self.number = number
        ## metto il nodo appena creato nella lista che li contiene tutti
        ## nota: quando si passa self, si passa l'intero oggetto, quando invece si passa self.parametro,
        ## si passa solo il valore di quel parametro 
        common.orderedListOfNodes.append(self)
        common.agents[self.number] = self
        self.myWorldState = myWorldState
        self.agType = agType
        ## assegno lo score a ciuscun agente in modo random 
        self.score = random.random()
        
        self.fake_news = False
        self.bias_right = False
        self.right = False
        self.right_leaning = False
        self.center = False
        self.left_leaning = False
        self.left = False
        self.bias_left = False

        self.debunker = False ## mi dice se è un debunker
        self.trust = {}

        if self.agType == "left_broadcasters":
            self.score = random.uniform(0.45,0.7)
            
        ## assegno lo score in base alle proporzioni di users
        if self.agType == "voters":
            common.voters_list.append(self)
            if self.number >= (common.number_of_left_broadcasters - 1) and self.number < ( common.number_of_left_broadcasters + common.fake_news_users ):
                self.score = random.uniform(0 , 0.1)
                self.fake_news = True
                common.fake_news_users_list.append(self)
            if self.number >= ( common.number_of_left_broadcasters + common.fake_news_users - 1 ) and self.number < ( common.number_of_left_broadcasters + common.fake_news_users + common.bias_right_users ):
                self.score = random.uniform(0.1 , 0.2)
                self.bias_right = True
                common.bias_right_users_list.append(self)
            if self.number >= ( common.number_of_left_broadcasters + common.fake_news_users + common.bias_right_users - 1 ) and self.number < ( common.number_of_left_broadcasters + common.fake_news_users + common.bias_right_users + common.right_users ):
                self.score = random.uniform(0.2 , 0.3)
                self.right = True
                common.right_users_list.append(self)
            if self.number >= ( common.number_of_left_broadcasters + common.fake_news_users + common.bias_right_users + common.right_users - 1 ) and self.number < ( common.number_of_left_broadcasters + common.right_leaning_users + common.fake_news_users + common.bias_right_users + common.right_users ):
                self.score = random.uniform(0.3 , 0.45)
                self.right_leaning = True
                common.right_leaning_users_list.append(self)
            if self.number >= ( common.number_of_left_broadcasters + common.fake_news_users + common.bias_right_users + common.right_users + common.right_leaning_users - 1 ) and self.number < ( common.number_of_left_broadcasters + common.right_leaning_users + common.fake_news_users + common.bias_right_users + common.right_users + common.center_users ):
                self.score = random.uniform(0.45 , 0.55)
                self.center = True
                common.center_users_list.append(self)
            if self.number >= ( common.number_of_left_broadcasters + common.fake_news_users + common.bias_right_users + common.right_users + common.right_leaning_users + common.center_users - 1 ) and self.number < ( common.number_of_left_broadcasters + common.fake_news_users + common.bias_right_users + common.right_users + common.right_leaning_users + common.center_users + common.left_leaning_users ):
                self.score = random.uniform(0.55 , 0.7)
                self.left_leaning = True
                common.left_leaning_users_list.append(self)
            if self.number >= ( common.number_of_left_broadcasters + common.fake_news_users + common.bias_right_users + common.right_users + common.right_leaning_users + common.center_users + common.left_leaning_users - 1 ) and self.number < ( common.number_of_left_broadcasters + common.fake_news_users + common.bias_right_users + common.right_users + common.right_leaning_users + common.center_users + common.left_leaning_users + common.left_users ):
                self.score = random.uniform(0.7 , 0.8)
                self.left = True
                common.left_users_list.append(self)
            if self.number >= ( common.number_of_left_broadcasters + common.fake_news_users + common.bias_right_users + common.right_users + common.right_leaning_users + common.center_users + common.left_leaning_users + common.left_users - 1 ):
                self.score = random.uniform(0.8 , 0.9)
                self.bias_left = True
                common.bias_left_users_list.append(self)
                
        if self.agType == "right_bots":
            self.score = random.uniform(0, 0.1)
            
        if self.agType == "left_bots":
            self.score = random.uniform(0.88, 0.9)
            
        if self.agType == "breitbart":
            self.score = 0.02


        self.xPos = 0
        self.yPos = 0
        
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
        ## lista che contiene l'is delle news che l'agente sa che sono fake
        self.fake = []
        
        # the graph
        if gvf.getGraph() == 0:
            gvf.createGraph()
            print("Creating the network with ", common.total_number_of_nodes," agents.")
            print("Voters and broadcasters: ", common.number_of_users)
            print("Bots: ", common.number_of_bots)
            # print("Broadcasters: ", common.number_of_left_broadcasters)



    def getGraph(self):
        return common.follower
    
    def renumber(self):
        self.number = common.shuffled_nodes_list[self.number]
        return   
        
    ## funzione che crea la news 
    def create_news(self):
        random.seed()
        if self in common.news_creator:
            ## assegno lo score della notizia in base allo score dell'agente 
            score = self.score
            ## aggiungo le feature della news al dizionario che contiene tutte le news 
            common.news.append({"id" : common.new_news_id , 
                                "autore" : self,
                                "score" : self.score,
                                "id autore" : self.number,
                                "agent type" : self.agType,
                                "retweet" : 0})    
            print("Agent ", self.number," of type ", self.agType," creating news ", common.new_news_id," with score ", score)
            
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
        score = self.score
        ## aggiungo le feature della news al dizionario che contiene tutte le news 
        common.news.append({"id" : common.new_news_id , 
                            "autore" : self,
                            "score" : self.score,
                            "id autore" : self.number,
                            "agent type" : self.agType,
                            "retweet" : 0})    
        print("Agent ", self.number," of type ", self.agType, " creating news ",common.new_news_id," with score ", score)
        
        send_news(self, common.new_news_id)
        common.new_news_id += 1
        
        
        return
    

    
    ## funzione per integrare la news che mi arriva 
    ## https://www.geeksforgeeks.org/python-find-dictionary-matching-value-in-list/
    def integrate_news(self):
        random.seed()
        try: # provo a integrare le news che mi sono appena arrivate
            for j in self.news_da_integrare:
                if len(j) == 2:
                    i = j[0]
                    sender = j[1]
                    ## seleziono la news dal dictionary che le contiene tutte 
                    for news in common.news:
                        if news["id"] == i:
                        ## estraggo le feature della news 
                            news_score = news["score"]
                            autore = news["autore"]
                            deb = True ## controllo di non aver fatto io stesso il debunking della news 
                            ## https://stackoverflow.com/questions/10406130/check-if-something-is-not-in-a-list-in-python
                            ## controllo che io non sia l'autore della news
                            ## controllo che non abbia già ricondiviso la news 
                            if autore != self and i not in self.news_integrate:
                                ## controllo che la news non sia fake
                                if self.debunker and news_score < 0.1 and common.prob_debunking > random.random(): ##and common.prob_debunking > random.random():
                                    self.fake.append(i) ## aggiungo la news fake tra quelle che conosco
                                    debunk(self, i, autore.number) ## dico ai miei vicini che quella news è fake
                                    big_change_trust(self, autore.number) ## se la news che mi arriva è fake e lo so, allora modifico la matrice di trust
                                    deb = False
                                    
                                if i in self.fake and deb: ## se la news che mi arriva è fake e lo so, allora modifico la matrice di trust
                                    big_change_trust(self, autore.number)
##                                    print("Agent", autore.number, " has sent me a fake news")
                                    return
                                ##le integro se lo score della news è abbastanza vicino al mio score e se mi fido abbastanza di chi retweetta la news
                                trst = self.trust.get(autore.number)
                                if trst is None:
                                    self.trust[autore.number] = 50
                                    trst = self.trust.get(autore.number)
##                                print(trst)
                                if abs(self.score - news_score) < random.random() and (trst / 100) > random.random(): 
                                    ## aggiungo l'id della news tra le news integrate
                                    self.news_integrate.append(i)
                                    ## se integro la news allora modifico il mio score a seconda 
                                    ## dello score della news integrata 
                                    self.score = self.score + ((news_score - 0.5) / 100 )
                                    ## mando la notizia ai miei follower
                                    send_news(self, i)
                                    ## uppo il contatore dei retweet
                                    news["retweet"] += 1
                                    ## creo il link   autore news -> self
                                    gvf.createEdge(autore.number, self.number)
                                    gvf.createEdge(sender, self.number)
                                    ## aumento il contatore delle news ricevute 
                                    self.counter_news_ricevute += 1
##                                    print("Integrated news")
                                    ## se integro la news, aumento il trust di chi me la manda 
                                    med_change_trust(self,autore.number)

      


        ## pulisco la lista delle news da integrare
            del self.news_da_integrare[:]

        except:
            print("Not done")
            return
        
        return


    ## funzione per integrare la news che arriva al bot
    ## https://www.geeksforgeeks.org/python-find-dictionary-matching-value-in-list/
    def bot_integrate_news(self):
        random.seed()
        to_integrate = False ## mi dice se devo integrare la news
        left = False ## mi dice se il bot è della fazione left
        if self.agType == "left_bots":
            left = True
            soglia = 0.8 #0.75
        if self.agType == "right_bots" or self.agType == "breitbart":
            soglia = 0.1
        try:
        # provo a integrare le news che mi sono appena arrivate
            for j in self.news_da_integrare:
                if len(j) == 2:
                    i = j[0]
                    sender = j[1]
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
                                if news_score <= soglia and not left:
                                    to_integrate = True
                                if news_score >= soglia and left:
                                    to_integrate = True
                                if to_integrate:
                            ## aggiungo l'id della news tra le news integrate
                                    self.news_integrate.append(i)
                            ## se integro la news allora modifico il mio score a seconda 
                            # ## dello score della news integrata 
                            # self.score = self.score + ((news_score - 0.5) / 100 )
                            ## mando la notizia ai miei follower
                                    send_news(self, i)
                                    gvf.createEdge(sender, self.number)
                            ## uppo il contatore dei retweet
                                    news["retweet"] += 1
                            ## creo un link con l'autore della news
                            # gvf.createEdge(self, autore)
                                    gvf.createEdge(autore.number, self.number)
                            ## aumento il contatore delle news ricevute 
                                    self.counter_news_ricevute += 1

                if len(j) == 1:
                    i = j
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
                                if news_score <= soglia and not left:
                                    to_integrate = True
                                if news_score >= soglia and left:
                                    to_integrate = True
                                if to_integrate:
                            ## aggiungo l'id della news tra le news integrate
                                    self.news_integrate.append(i)
                            ## se integro la news allora modifico il mio score a seconda 
                            # ## dello score della news integrata 
                            # self.score = self.score + ((news_score - 0.5) / 100 )
                            ## mando la notizia ai miei follower
                                    send_news(self, i)
                            ## uppo il contatore dei retweet
                                    news["retweet"] += 1
                            ## creo un link con l'autore della news
                            # gvf.createEdge(self, autore)
                                    gvf.createEdge(autore.number, self.number)
                            ## aumento il contatore delle news ricevute 
                                    self.counter_news_ricevute += 1

                            
        ## pulisco la lista delle news da integrare 
            del self.news_da_integrare[:]

        except:
            return
            
        return   
    
    def dictionary(self):
        common.all_parameters.append({"id_autore" : self.number,
                                      "agent_type" : self.agType,
                                      "score" : self.score})
        return    
    
    def dictionary_init(self):
        common.inizial_parameters.append({"id_autore" : self.number,
                                      "agent_type" : self.agType,
                                      "score" : self.score})
        return

    def trust_init(self):
        try:
            my_id = common.follower.GetNI(self.number)
            for node in my_id.GetInEdges():
                other_node = common.agents[node]
                self.trust[other_node.number] = 50 ## inizializzazione del trust uniforme
            # print(self.trust)
        except BaseException:
            print("init not done")
            return

        return

## calcola la somma dei degree di tutti i nodi 
def totaldegree(): ## funziona 
    totaldegree = 0
    for i in common.orderedListOfNodes:
        totaldegree += common.follower.degree[i]   
    return totaldegree  


## funzione che serve per inviare la news 
def send_news(self, news_to_send):
    done = False ## serve per controllare se il nodo ha dei neighbors o no 
    try:
        ## seleziono i destinatari della news =  i miei follower 
        my_id = common.follower.GetNI(self.number)
        for node in my_id.GetOutEdges():
            # print("Sending news to  ", node)
            ## aggiungo l'id della news alla lista delle news ricevute del mio follower
            ## devo accedere all'oggetto con id node
            receiver = common.agents[node]
            #gvf.createEdge(self.number, receiver.number)
            # print("receiver ", receiver)
            receiver.news_ricevute.append(news_to_send)   
            ## aggiungo l'id della news alla lista delle news da integrare del mio follower
            receiver.news_da_integrare.append([news_to_send, self.number])   
            done = True 
            
        ## se il nodo selezionato non ha follower, allora sceglie un nodo a caso e la manda a lui        
        if not done:
            i = random.choice(common.orderedListOfNodes)
            # print("Sending news to  ", i.number)
            ## aggiungo l'id della news alla lista delle news ricevute dal destinatario
            i.news_ricevute.append(news_to_send)
            ## aggiungo l'id della news alla lista delle news da integrare del mio follower
            i.news_da_integrare.append([news_to_send, self.number])
                   
    except BaseException:
        print("Not sent")        
     
    return



def debunk(self, news, autore):
    try:
        aut = autore
        my_id = common.follower.GetNI(self.number)
        for node in my_id.GetInEdges():
            receiver = common.agents[node]
            receiver.fake.append(news) ## dico ai miei vicini che quella news è fake
            small_change_trust(receiver, aut, self)
##            print("debunkin")

    except:
        print("debunk not done")
        return
    return

def big_change_trust(self, autore):
    try:
        trst = self.trust.get(autore)
        if trst is None:
            self.trust[autore] = 50
            trst = self.trust[autore]
        if trst > common.big_penalty :
            self.trust[autore] = trst - common.big_penalty 
    except:
        print("Big change not done")
    return

def med_change_trust(self, autore):
    try:
        trst = self.trust.get(autore)
        if trst is None:
            self.trust[autore] = 50
            trst = self.trust[autore]
        if trst < 100 - common.big_penalty :
            self.trust[autore] = trst + common.med_penalty 
    except:
        print("Med change not done")
    return


def small_change_trust(self, autore, deb):
    try:
        trst = self.trust.get(autore)
        if trst is None:
            self.trust[autore] = 50
            trst = self.trust[autore]
        if trst > common.small_penalty :
            self.trust[autore] = trst - common.small_penalty ## diminuisco il trust di chi mi ha girato la fake news
    ##        print("Small change in trust")
        trst_deb = self.trust.get(deb.number)
        if trst_deb is None:
            self.trust[deb] = 50
            trst_deb = self.trust[deb] 
        if trst_deb < 100 +  common.small_penalty:
            self.trust[deb.number] = trst_deb + common.small_penalty ## aumento il trust di chi mi ha detto che la news era fake

    except:
        print("small change not done")
    return
