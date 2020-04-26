import networkx as nx
import matplotlib.pyplot as plt
import commonVar as common


# the base: creating the graph (and copying its address in a common variable
# to have the possibility of direct interaction with the graph when
# the program is finished, as the common space is imported also in the main
# program
def createGraph():
    global colors, pos

    ## creo il grafo, assegnandolo alla variabile g definita in commonVar.py 
    common.g = nx.DiGraph()  # directed graph, instead of nx.Graph()
    colors = {}
    pos = {}
    common.g_labels = {}
    common.g_edge_labels = {}  # copy the address of the labels of the edges


## creo un link tra i nodi a e b 
def createEdge(a, b):
    # implicitly directed, due to the use of DiGraph
    if a is None or b is None:
        print("Internal error, attempt to create an edge with a node defined None")
        exit(0)

    try:
        common.g[a][b]['weight'] = 1 + common.g[a][b]['weight']
    except BaseException:
        common.g.add_edge(a, b)
        common.g[a][b]['weight'] = 1

    if a != b:
        # verifying the presence of the edge in the other direction
        try:
            otherW = common.g[b][a]['weight']
            common.g_edge_labels[a, b] = "w.s %d and %d" % (
                common.g[a][b]['weight'], otherW)
            common.g_edge_labels[b, a] = ""
        except BaseException:
            common.g_edge_labels[a, b] = "w. %d" % common.g[a][b]['weight']

    if a == b:
        common.g_edge_labels[a, b] = ""
        common.g[a][b]['pseudoLabel'] = "auto link w. %d" \
            % common.g[a][b]['weight']


# using networkX and matplotlib case
def closeNetworkXdisplay():
    plt.close()


def openClearNetworkXdisplay():
    if common.graphicStatus == "PythonViaTerminal":
        plt.ion()
    # plt.clf()


def clearNetworkXdisplay():
    plt.clf()


def getGraph():
    try:
        return common.g
    except BaseException:
        return 0


## funzione che crea il grafo 
def drawGraph():

    clearNetworkXdisplay()
    # nx.draw_networkx(common.g, pos, font_size=10, node_size=500, labels=common.g_labels)
    # nx.draw_networkx_edge_labels(common.g, pos, edge_labels=common.g_edge_labels, font_size=9)
    for i in common.orderedListOfNodes:
        if i.score > 0.5:
            common.colordict[i] = 'b'
        if i.score <= 0.5:
            common.colordict[i] = 'r'
    if not common.PA_done:
        nx.draw_networkx(common.g, pos, font_size=10, node_size=500, node_color = [v for v in common.colordict.values()],  labels=common.g_labels)
    if common.PA_done:
        # d = nx.degree(common.g)
        d = dict(common.g.degree) 
        nx.draw_networkx(common.g, pos = nx.spring_layout(common.g), font_size=10, node_size = [ v * 10 for v in d.values()] ,  node_color = [v for v in common.colordict.values()], labels=common.g_labels)

        # nx.draw_networkx(common.g, pos, font_size=10, node_size = [ v * 10 for v in d.values()] ,  node_color = [v for v in common.colordict.values()], labels=common.g_labels)
    # nx.draw_networkx_edge_labels(common.g, pos)
    # plt.draw()
    plt.show()  # used by %Matplotlib inline [without ion()]; not conflicting
    # with ion()

    if common.graphicStatus == "PythonViaTerminal":
        plt.pause(0.01)
    # to show the sequence of the shown images in absence of pauses

    # print agentGraph.nodes(data=True)
    # print agentGraph.edges(data=True)
    # print labels
    # print edge_labels

    # print a, agentGraph.node[a].keys(), agentGraph.node[a].values(),\
    #      agentGraph.node[a]['sector']

    if common.analysis:
    # adjacency
    ## stampa la matrice di adiacenza
        print()
        for i in range(len(common.orderedListOfNodes)):
            print("%d " % common.orderedListOfNodes[i].number, end=' ')
            print()
    # print "drawGraph verification of existing nodes",common.g.nodes()
        if common.g.nodes() != []:
            A = nx.adjacency_matrix(common.g, nodelist=common.orderedListOfNodes, weight='weight')
        # print A          # as sparse matrix, defaul from nx 1.9.1
            print(A.todense())  # as a regular matrix

        else:
            print("No nodes, impossible to create the adjacency_matrix")
            print()

    ## NON FUNZIONA 
    # # neighbors
    # ## stampa i nodi a cui il nodo selezionato è collegato 
    # for aNode in common.g.nodes():
    #     print(aNode.number, [node.number
    #                           for node in nx.neighbors(common.g, aNode)])

    # betweenness_centrality
    # Betweenness centrality of a node v is the sum of the fraction of all-pairs
    # shortest paths that pass through v
    # http://networkx.lanl.gov/reference/generated/
    # networkx.algorithms.centrality.betweenness_centrality.html
        print()
        print("betweenness_centrality")
        common.btwn = nx.betweenness_centrality( common.g, normalized=False, weight='weight')
    # print btw
    ## stampa la betweenness per ogni nodo 
        for i in range(len(common.orderedListOfNodes)):
            print(common.orderedListOfNodes[i].number, common.btwn[common.orderedListOfNodes[i]])

    # closeness_centrality
    # Closeness centrality at a node is 1/average distance to all other nodes
    # http://networkx.lanl.gov/reference/generated/
    # networkx.algorithms.centrality.closeness_centrality.html
        print()
        print("closeness_centrality")
        common.clsn = nx.closeness_centrality(common.g)
    # print clsn
    ## stampa la closeness per ogni nodo
        for i in range(len(common.orderedListOfNodes)):
            print(common.orderedListOfNodes[i].number, common.clsn[common.orderedListOfNodes[i]])
