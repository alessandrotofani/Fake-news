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
            if i.score == 0:
                i.score = random.random()
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

    elif subStep == "assortative" and common.assortative:
        common.assortative = False
        print("creating assortative graph")
        n_nodes = [] ## list of total number of nodes per fazione
        n_nodes.append(common.fake_news_users)
        n_nodes.append(common.bias_right_users)
        n_nodes.append(common.right_users)
        n_nodes.append(common.right_leaning_users)
        n_nodes.append(common.center_users)
        n_nodes.append(common.left_leaning_users)
        n_nodes.append(common.left_users)
        n_nodes.append(common.bias_left_users)
        print(n_nodes)

        scores = [] ## max score per fazione
        scores.append(0)
        scores.append(0.1)
        scores.append(0.2)
        scores.append(0.3)
        scores.append(0.45)
        scores.append(0.55)
        scores.append(0.7)
        scores.append(0.8)
        scores.append(0.9)
        print(scores)
        
        current_nodes = [] ## lista che contiene i nodi correnti di ogni fazione
        ## creo l'algoritmo in modo che possa essere ripetuto per ogni fazione senza specificare
        ## a priori la fazione con cui si sta lavorando
        for i in range(8):
            print("Step ", i)
            current_nodes.append(0)
            tot_nodes = n_nodes[i]
            choose = True
            while choose:
                node = random.choice(common.voters_list)
                # print(node)
                if node.score == 0:
                    choose = False
                    # print("node chosen")
                   
            while current_nodes[i] < tot_nodes:
                if node.score == 0:
                    node.score = random.uniform(scores[i], scores[i+1])
                    current_nodes[i] += 1
                    # print(current_nodes)
                    my_id = common.follower.GetNI(node.number)
                    # print(my_id)
                    temp = 0
                    for vicino in my_id.GetOutEdges():
                        if temp == 0:
                            neighbor_agent = common.agents[vicino]
                            node = neighbor_agent
                            temp = 1
                else:
                    node = random.choice(common.voters_list)

            print("Nodi ", current_nodes)
            print("Nodi totali ", n_nodes)
                
    

            


##funzione per salvare i dati che va a prendere il dizionario creato
##alla fine della schedule e definito nel file Agent.py
def saveData():

    dataset = pd.DataFrame.from_dict(common.all_parameters)
    dataset.to_csv("data.csv", index=False)
    dataset_init = pd.DataFrame.from_dict(common.inizial_parameters)
    dataset_init.to_csv("data_init.csv", index=False)
    
