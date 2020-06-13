from Tools import *
from Agent import *
import graphicDisplayGlobalVarAndFunctions as gvf
import pandas as pd
import snap
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
    gvf.openCleardisplay()
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
    
    elif subStep == "random":
        common.news_creator = random.randint(1, common.total_number_of_nodes)   
        return True
    elif subStep == "restart":
        del common.fake_news_users_list[:]        
        del common.bias_right_users_list[:]        
        del common.right_users_list[:]        
        del common.right_leaning_users_list[:]        
        del common.center_users_list[:]        
        del common.left_leaning_users_list[:]        
        del common.left_users_list[:]        
        del common.bias_left_users_list[:]
        return True

    elif subStep == "check":
        for i in common.voters_list:
            i.fake_news = False
            i.bias_right = False
            i.right = False
            i.right_leaning = False 
            i.center = False
            i.left_leaning = False
            i.left = False
            i.bias_left = False
            if i.score < 0.1:
                i.fake_news = True
                common.fake_news_users_list.append(i)
            if i.score >=0.1 and i.score < 0.2:
                i.bias_right = True
                common.bias_right_users_list.append(i)
            if i.score >= 0.2 and i.score < 0.3:               
                i.right = True
                common.right_users_list.append(i)
            if i.score >= 0.3 and i.score < 0.45:
                i.right_leaning = True
                common.right_leaning_users_list.append(i)
            if i.score >= 0.45 and i.score < 0.55:
                i.center = True
                common.center_users_list.append(i)
            if i.score >= 0.55 and i.score < 0.7:
                i.left_leaning = True
                common.left_leaning_users_list.append(i)
            if i.score >= 0.7 and i.score < 0.8:
                i.left = True
                common.left_users_list.append(i)
            if i.score >= 0.8:
                i.bias_left = True
                common.bias_left_users_list.append(i)

        return True
            


##funzione per salvare i dati che va a prendere il dizionario creato
##alla fine della schedule e definito nel file Agent.py
def saveData():

    dataset = pd.DataFrame.from_dict(common.all_parameters)
    dataset.to_csv("data.csv", index=False)
    dataset_init = pd.DataFrame.from_dict(common.inizial_parameters)
    dataset_init.to_csv("data_init.csv", index=False)
    
