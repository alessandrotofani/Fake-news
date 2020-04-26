from Tools import *
from Agent import *
import graphicDisplayGlobalVarAndFunctions as gvf
import commonVar as common


## serve per il debug 
## nel modello non fa nulla 
def do1b(address):

    # to debug, having the map of the agent
    agL = []
    for ag in address.modelSwarm.agentList:
        agL.append(ag.number)
    agL.sort()
    # print "\noActions before drawGraph agents", agL
    # print "oActions before drawGraph nodes", common.g.nodes()

    # basic action to visualize the networkX output
    gvf.openClearNetworkXdisplay()
    gvf.drawGraph()


## implementazione dell'ask_all 
## chiede a tutti gli agenti di riportare la posizione 
## l'ask_all non compare in observerActions.txt, quindi non è usata in tale modello
def do2a(address, cycle):
    self = address  # if necessary

    # ask each agent, without parameters

    print("Time = ", cycle, "ask all agents to report position")
    askEachAgentInCollection(
        address.modelSwarm.getAgentList(),
        Agent.reportPosition)


## implementazione dell'ask_one
## chiede a un agente di riportare la posizione 
## l'ask_one non compare in observerActions.txt, quindi non è usata in tale modello
def do2b(address, cycle):
    self = address  # if necessary

    # ask a single agent, without parameters
    print("Time = ", cycle, "ask first agent to report position")
    if address.modelSwarm.getAgentList() != []:
        askAgent(address.modelSwarm.getAgentList()[0],
                 Agent.reportPosition)


## implementa gli altri step in observerActions.txt
def otherSubSteps(subStep, address):

    ## implementa pause: fermo il modello, e devo schiacciare enter per proseguire 
    if subStep == "pause":
        input("Hit enter key to continue")
        return True

    ## implementa prune: elimina i link che hanno peso inferiore alla prune.Threshold
    ## nota che la pruneThreshold è definita in commonVar.py 
    elif subStep == "prune":
        common.prune = True
        newValue = input(("Prune links with weight < %d\n" +
                          "Enter to confirm " +
                          "or introduce a new level: ") %
                         common.pruneThreshold)
        if newValue != "":
            common.pruneThreshold = int(newValue)
        return True

    else:
        return False
