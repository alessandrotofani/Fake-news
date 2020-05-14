import random 
import math
## tutorial sui dictionary
## https://www.w3schools.com/python/python_dictionaries.asp

## NODE SECTION
## numero totale di nodi nel network
total_number_of_nodes = 100
users = 0.96 * total_number_of_nodes
number_of_users = math.floor(users)
number_of_bots = total_number_of_nodes - number_of_users

links_per_node = 3 ## è il numero di link che ogni nodo formerà 
orderedListOfNodes = []
connectednodes= [] ## lista con i nodi che hanno grado diverso da zero 
nodesdegree = [] ## lista che contiene i gradi dei nodi


## GRAPH SECTION
g = 0  # this variable will contain the address of the graph
g_labels = 0  # this variable will contain the address of the labels
g_edge_labels = 0  # this variable will contain the address of the labels of the edges
# size of the pictures
width = 20
height = 30
colordict = {} ## dzionario che contiene (nodo : colore)

##NEWS SECTION
news = []
news_creator = random.randint(1, total_number_of_nodes) ## id dell'autore della news 
## lo uppo in drawGraph() ## probabilmente non è la cosa più elegante da fare 
new_news_id = 0 ## contatore che mi dice quante news ho creato fino ad ora,
## servirà per assegnare l'id delle news create 

## BOOL SECTION
everything_done = True
scale_free_test = True ## dice se lo scale free test deve essere fatto o no 
PA_done = False ## mi dice se ho finito il preferential attachment
analysis = True 
verbose = False

## ANALYSIS SECTION
btwn = 0  # this variable will contain the betweenness centrality indicators
clsn = 0  # this variable will contain the closeness centrality indicators
degreefrequency = {} ## dizionario che contiene la frequenza di un dato grado 


## MISCELLANEA SECTION
prob = 0
clonedN = 0
prune = False
pruneThreshold = 0
prova = 0


