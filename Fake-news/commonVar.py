import random 
import math
## tutorial sui dictionary
## https://www.w3schools.com/python/python_dictionaries.asp

## NODE SECTION
## numero totale di nodi nel network
total_number_of_nodes = 10000
users = 0.96 * total_number_of_nodes
number_of_users = math.floor(users)
number_of_left_broadcasters = 4
number_of_bots = total_number_of_nodes - number_of_users

fake_news_users = 0.01 * number_of_users
fake_news_users_list = []
n_fake = 5
bias_right_users = 0.07 * number_of_users
bias_right_users_list = []
n_biasright = 5
right_users = 0.10 * number_of_users
right_users_list = []
n_right = 3
right_leaning_users = 0.06 * number_of_users
right_leaning_users_list = []
n_right_leaning = 1
center_users = 0.24 * number_of_users
center_users_list = []
n_center = 2
left_leaning_users = 0.30 * number_of_users
left_leaning_users_list = []
n_leftleaning = 2
left_users = 0.16 * number_of_users
left_users_list = []
n_left = 2
bias_left_users = 0.02 * number_of_users
bias_left_users_list = []
n_left = 2
links_per_node = 1 ## è il numero di link che ogni nodo formerà 
orderedListOfNodes = []
agents = {}
connectednodes= [] ## lista con i nodi che hanno grado diverso da zero 
nodesdegree = [] ## lista che contiene i gradi dei nodi


## GRAPH SECTION
h = 0
g = 0  # this variable will contain the address of the graph
g_labels = 0  # this variable will contain the address of the labels
g_edge_labels = 0  # this variable will contain the address of the labels of the edges
# size of the pictures
width = 20
height = 30
colordict = {} ## dzionario che contiene (nodo : colore)
start = True ## bool che mi serve per salvare il network iniziale e finale 

##NEWS SECTION
news = []
# news_creator = random.randint(1, total_number_of_nodes) ## id dell'autore della news 
news_creator = random.sample(range(4, number_of_users), 3) ## lista con l'id dell'autore della news 
## lo uppo in drawGraph() ## probabilmente non è la cosa più elegante da fare 
new_news_id = 0 ## contatore che mi dice quante news ho creato fino ad ora,
## servirà per assegnare l'id delle news create 


## BOOL SECTION
everything_done = True
scale_free_test = True ## dice se lo scale free test deve essere fatto o no 
PA_done = True ## mi dice se ho finito il preferential attachment
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


