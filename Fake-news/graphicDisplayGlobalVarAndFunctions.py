import matplotlib.pyplot as plt
import commonVar as common
import numpy as np
import pandas as pd
import snap 
import random 
import graphviz
from graphviz import Source


# the base: creating the graph (and copying its address in a common variable
# to have the possibility of direct interaction with the graph when
# the program is finished, as the common space is imported also in the main
# program
def createGraph():
    global colors, pos

    ## creo il grafo, assegnandolo alla variabile g definita in commonVar.py 
    Rnd = snap.TRnd()
    Rnd.Randomize()
    ## http://snap.stanford.edu/snappy/doc/reference/GenForestFire.html
    forward = 0.37 ## provare con 0.51,0.16
    backward = 0.32 ## anche 0.16
    ## follower network -> l'esponente dovrebbe essere circa 1.87
    common.follower = snap.GenForestFire(common.total_number_of_nodes, forward, backward)
    ## information network -> l'esponente dovrebbe essere circa 2.2
    common.information = snap.TNGraph.New()
    ## https://snap.stanford.edu/snappy/#types
    for i in range(common.total_number_of_nodes):
        if i == 0:
            print("inserting nodes")
        common.information.AddNode(i) ## aggiungo i nodi all'information network
        common.shuffled_nodes_list.append(i)

    random.shuffle(common.shuffled_nodes_list)
    
    
    print("Forward burning probability: ", forward) 
    print("Backward burning probability: ", backward) 
    print(" Networks created")



## https://networkx.github.io/documentation/stable/auto_examples/drawing/plot_weighted_graph.html
## creo un link tra i nodi a e b 
def createEdge(a, b):
    # implicitly directed, due to the use of DiGraph
    if a is None or b is None:
        print("Internal error, attempt to create an edge with a node defined None")
        exit(0)
    try:
       ## if not IsEdge(a,b):
        common.follower.AddEdge(a,b)
        common.information.AddEdge(a,b)
        common.trust[a,b] = 50
            ## https://snap.stanford.edu/snappy/doc/reference/graphs.html
    except BaseException:
        return


# using networkX and matplotlib case
def closeNetworkXdisplay():
    plt.close()


def openCleardisplay():
    if common.graphicStatus == "PythonViaTerminal":
        plt.ion()
    # plt.clf()


def cleardisplay():
    plt.clf()


def getGraph():
    try:
        return common.follower
    except BaseException:
        return 0
    
def choose_news_creator(lista, n):
    i = 0 
    while i < n:
        common.news_creator.append(random.choice(lista))
        i += 1         
    return


## funzione che crea il grafo 
def drawGraph():

    ## pulisco la lista con i news creators
    del common.news_creator[:] 
    ## assegno i news creator riempiendo le rispettive liste 
    choose_news_creator(common.fake_news_users_list, common.n_fake)
    choose_news_creator(common.bias_right_users_list, common.n_biasright)
    choose_news_creator(common.right_users_list, common.n_right)
    choose_news_creator(common.right_leaning_users_list, common.n_right_leaning)
    choose_news_creator(common.center_users_list, common.n_center)
    choose_news_creator(common.left_leaning_users_list, common.n_leftleaning)
    choose_news_creator(common.left_users_list, common.n_left)
    choose_news_creator(common.bias_left_users_list, common.n_left)

    cleardisplay()
    ## coloro i nodi a seconda dello score 
    ## https://snap.stanford.edu/snappy/doc/reference/DrawGViz.html
    NIdColorH = snap.TIntStrH()
    for i in common.orderedListOfNodes:
        if i.score > 0.5:
            NIdColorH[i.number] = 'blue'
        if i.score <= 0.5:
            NIdColorH[i.number] = 'red'    
    ## hash table con le labels        
    labels = snap.TIntStrH()
    for NI in common.follower.Nodes():
        labels[NI.GetId()] = str(NI.GetId())
    if common.PA_done:
        ## salvo nel file .dot le net iniziali 
        if common.start: 
            snap.SaveGViz(common.follower, "follower_network_iniziale.dot", "Directed Graph", True, NIdColorH)
            snap.SaveGViz(common.information, "information_network_iniziale.dot", "Directed Graph", True, NIdColorH)
            common.start = False
        ## salvo nel file .dot le net finali 
        if not common.start:
            snap.SaveGViz(common.follower, "follower_network_finale.dot", "Directed Graph", True, NIdColorH)
            snap.SaveGViz(common.information, "information_network_finale.dot", "Directed Graph", True, NIdColorH)
            
    if common.graphicStatus == "PythonViaTerminal":
        plt.pause(0.01)
    # to show the sequence of the shown images in absence of pauses

