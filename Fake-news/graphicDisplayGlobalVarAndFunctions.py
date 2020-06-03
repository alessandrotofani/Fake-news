import matplotlib.pyplot as plt
import commonVar as common
import numpy as np
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
    # common.h = snap.GenRndPowerLaw(common.total_number_of_nodes, 2)  
    # Rnd = snap.TRnd()
    # Rnd.Randomize()
    # common.h = snap.GenRndPowerLaw(common.total_number_of_nodes, 3, True, Rnd)  
    # common.g = snap.ConvertGraph(snap.PNGraph, common.h)
    common.g = snap.GenForestFire(common.total_number_of_nodes, 0.37, 0.32) ## 0.37, 0.32
    # for EI in common.g.Edges():
    #     print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))
    print(" Network created")
    # colors = {}
    # pos = {}
    # common.g_labels = {}
    # common.g_edge_labels = {}  # copy the address of the labels of the edges


## https://networkx.github.io/documentation/stable/auto_examples/drawing/plot_weighted_graph.html
## creo un link tra i nodi a e b 
def createEdge(a, b):
    # implicitly directed, due to the use of DiGraph
    if a is None or b is None:
        print("Internal error, attempt to create an edge with a node defined None")
        exit(0)

    try:
        common.g.AddEdge(a,b)
        # print("edge created")
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
        return common.g
    except BaseException:
        return 0



## funzione che crea il grafo 
def drawGraph():

    # common.news_creator = random.randint(1, common.number_of_users)  
    common.news_creator = random.sample(range(4, common.number_of_users), 3)
    cleardisplay()
    ## coloro i nodi a seconda dello score 
    # https://snap.stanford.edu/snappy/doc/reference/DrawGViz.html
    NIdColorH = snap.TIntStrH()
    for i in common.orderedListOfNodes:
        if i.score > 0.5:
            NIdColorH[i.number] = 'blue'
        if i.score <= 0.5:
            NIdColorH[i.number] = 'red'    
            
    labels = snap.TIntStrH()
    for NI in common.g.Nodes():
        labels[NI.GetId()] = str(NI.GetId())
    if common.PA_done:
        # d = dict(common.g.degree) ## dizionario che contiene il grado dei nodi
        ## disegno i nodi con grandezza proporizionale al proprio grado 
        # print(" The network ")
        ## https://snap.stanford.edu/snappy/doc/reference/DrawGViz.html
        # snap.DrawGViz(common.g, snap.gvlDot, "output.png", " ", labels, NIdColorH) ## crea il file png output nella cartella snap, che è la rete
        # snap.DrawGViz(common.g, snap.gvlDot, "out.png", " ", True, NIdColorH) ## crea il file png output nella cartella snap, che è la rete
        # snap.SaveEdgeList(common.g, 'mygraph.txt')
        if common.start: 
            snap.SaveGViz(common.g, "network_iniziale.dot", "Directed Graph", True, NIdColorH)
            common.start = False 
        # path = 'C:/Users/Alessandro/snap/out.png'
        # s = Source.from_file(path)
        # s.view()    
    # plt.show()      
        if not common.start:
            snap.SaveGViz(common.g, "network_finale.dot", "Directed Graph", True, NIdColorH)
            
    if common.graphicStatus == "PythonViaTerminal":
        plt.pause(0.01)
    # to show the sequence of the shown images in absence of pauses

