from Tools import *
from Agent import *
import os
import random
import commonVar as common


## implementa il reset 
def do0(address):
    self = address  # if necessary
    askEachAgentInCollection(address.agentList, Agent.setNewCycleValues)


## implementa il move 
## in questo caso fa lo shuffle degli agenti 
def do1(address):
    self = address  # if necessary

    # keep safe the original list
    address.agentListCopy = address.agentList[:]
    random.shuffle(address.agentListCopy)


## funzione che crea gli agenti 
## le funzioni che lavorano con l'agentlist sono in agTools.py
def createTheAgent(self, line, num, agType):
    # explicitly pass self, here we use a function

    ## gli agenti sono definiti nei rispettivi file txt
    # recipes
    ## le recipes sono definite solo da un numero, quindi 
    ## posso selezionarle dicendo che la loro lunghezza, una volta splittato il documento, è 1
    if len(line.split()) == 1:
        anAgent = Agent(num, self.worldState, agType=agType)
        self.agentList.append(anAgent)
        anAgent.setAgentList(self.agentList)

        ## aggiungo l'agente appena creato alla agentList, tramite la funzione append 
        self.agentList.append(anAgent)
        ## setto che la AgentList dell'agente appena creato, è quella che lo contiene
        anAgent.setAgentList(self.agentList)

    else:
        print("Error in file " + agType + ".txt")
        os.sys.exit(1)



def modPosition():
    if random.randint(0, 1) == 0:
        return random.randint(-8, -6)
    else:
        return random.randint(6, 8)


def otherSubSteps(subStep, address):

    if subStep == "addAFactory":
        addAFactory(address)
        return True

    if subStep == "removeAFactory":
        removeAFactory(address)
        return True

    else:
        return False
