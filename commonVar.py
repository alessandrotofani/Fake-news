prune = False
pruneThreshold = 0

# debug=True

g = 0  # this variable will contain the address of the graph
g_labels = 0  # this variable will contain the address of the labels
g_edge_labels = 0  # this variable will contain the address of the labels of the edges

btwn = 0  # this variable will contain the betweenness centrality indicators
clsn = 0  # this variable will contain the closeness centrality indicators

links_per_node = 3 ## è il numero di link che ogni nodo formerà 
prob = 0
PA_done = False ## mi dice se ho finito il preferential attachment
orderedListOfNodes = []
connectednodes= [] ## lista con i nodi che hanno grado diverso da zero 
colordict = {} ## dzionario che contiene (nodo : colore)
verbose = False
clonedN = 0

# size of the pictures
width = 20
height = 30
# width = 10
# height = 9.5  # in inches, but ... on paper
# and on the screen the effct is
# related to the screen
# and printer pixel density
# suggested ratio 3/2

analysis = True 
