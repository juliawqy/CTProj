# helper class

class Graph:
    __access = 0  # total number of accessment to the graph data, which is used to evaluate your efficiency
    __access_norm = 10000

    __required_jobs = 3  # required number of different jobs in invitees

    __node_num = 0  # number of nodes (friends) in the graph
    __edge_num = 0  # number of edges (conflict relationships) in the graph
    __jobs = []  # __jobs[n] denotes the job of node n
    __job_num = 0  # number of different jobs in the graph
    __edge_list = []  # __edge_list[n][i] denotes the i-th neighbor of node n

    __invitees = []  # __invitees[n] == True: friend n is invited to the party

    def __init__(self, dataset: str):  # reading test case files and initialization
        with open(dataset, 'r') as f:
            nnum = int(f.readline())
            enum = 0

            self.__node_num = nnum

            job_line = f.readline()
            job_line = job_line.split(' ')
            for i in range(nnum):
                self.__jobs.append(int(job_line[i]))

            for i in range(nnum):
                self.__edge_list.append([])

            eline = f.readline()
            while eline:
                if ' ' in eline:
                    eline = eline.split(' ')
                    node0 = int(eline[0])
                    node1 = int(eline[1])
                    self.__edge_list[node0].append(node1)
                    self.__edge_list[node1].append(node0)
                    enum += 1
                eline = f.readline()

        for i in range(nnum):
            self.__edge_list[i].sort()
        self.__invitees = [False for _ in range(nnum)]

        self.__edge_num = enum
        self.__job_num = max(self.__jobs) + 1

    def getNodeNum(self): ##total number of nodes returned
        return self.__node_num

    def getEdgeNum(self): ##total number of edges in the graph
        return self.__edge_num

    def getJobNum(self): ##total number of unique jobs in the graph
        return self.__job_num

    def getJobs(self, node: int): ##returns the Job of the node
        self.__access += 1
        return self.__jobs[node]

    def getDegree(self, node: int): ##returns the degree of the node, i.e., how many nodes are connected to it
        self.__access += 1
        return len(self.__edge_list[node])

    def getEdge(self, node: int, index: int): ##the index is reinitialised for every call
        self.__access += 1
        return self.__edge_list[node][index]

    def getInvitee(self): ##
        return self.__invitees

    def setInvitee(self, node: int):  # invite friend represented by "node"
        self.__invitees[node] = True

    def setInviteeFromList(self, node_list):
        for ni in node_list:
          # each element in node_list should be an integer in the range [0, node_num-1]
          if isinstance(ni, int) and ni >= 0 and ni < self.getNodeNum():
              self.setInvitee(ni)

    def isIndependentSet(self):  # check wether the current result is an independent set
        invitee_array = []
        for n in range(len(self.__invitees)):
            if self.__invitees[n]:
                invitee_array.append(n)

        for n in invitee_array:
            for nbr in self.__edge_list[n]:
                if self.__invitees[nbr]:
                    print("error: not a independent set")
                    return False
        return True

    def enoughJobs(self):
        selected_jobs = set()
        for n in range(len(self.__invitees)):
            if self.__invitees[n]:
                selected_jobs.add(self.__jobs[n])
        if len(selected_jobs) >= self.__required_jobs:
            return True
        else:
            print("error: not enough jobs")
            return False

    def score(self):  # the function used for evaluation
        invitee_num = 0
        for n in range(len(self.__invitees)):
            if self.__invitees[n]:
                invitee_num += 1

        is_independent_set = self.isIndependentSet()
        enough_job = self.enoughJobs()
        print("Number of invitees: " + str(invitee_num) + "\n")
        print("Self access:" + str(self.__access) + "\n")
        grades = invitee_num - (self.__access / self.__access_norm)
        if is_independent_set and enough_job:
            return grades
        else:
            if is_independent_set:
              if self.getNodeNum() < 500:
                return max(grades - 2,0)
              else:
                return max(grades - 4,0)
            else:
              return 0

def deleteNode(listOfDict, node): # list of dict is the graphDict, numDict, nodeNumDict

    # graphDict = listOfDict[0].copy()  #key = node ; val = neighbors
    # numDict = listOfDict[1].copy() # key = number of neighbors; val = nodes with those number of neighbors
    # nodeNumDict = listOfDict[2].copy() #key = node; val = number of neighbors

    graphDictNew = {}
    numDictNew = {}
    nodeNumDictNew = {}

    for key, value in listOfDict[0].items():
        newKey = int(key)
        newValue = list(value)
        graphDictNew[newKey] = newValue
    for key, value in listOfDict[1].items():
        newKey = int(key)
        newValue = list(value)
        numDictNew[newKey] = newValue
    for key, value in listOfDict[2].items():
        newKey = int(key)
        newValue = int(value)
        nodeNumDictNew[newKey] = newValue
    
    neighbors = graphDictNew[node] #gets those neighbors to reduce
    temp1 = numDictNew[len(neighbors)]
    temp1.remove(node)
    numDictNew[len(neighbors)] = temp1 #removes the node to remove from numDict
    
    del nodeNumDictNew[node] #removes the node from the nodeNumDict RIP    
    del graphDictNew[node] #removes the node from the graph dictionary RIP
    
    
    
    for neighbor in neighbors:
        #now we reducing all the neighbors of the removed node
        #graphDict
        temp2 = graphDictNew[neighbor]
        temp2.remove(node)
        graphDictNew[neighbor] = temp2
        
        #numDict
        afterCount = len(temp2)
        
        beforeCount = afterCount+1
        
        #remove from Before Count
        
        temp3 = numDictNew[beforeCount]
        
        
        if len(temp3) == 1:
            del numDictNew[beforeCount]
        else:
            temp3.remove(neighbor)
            numDictNew[beforeCount] = temp3
        
        #add in After Count
        if afterCount in numDictNew:
            numDictNew[afterCount]+= [neighbor]
        else:
            numDictNew[afterCount] = [neighbor]
        

        #nodeNumDict
        nodeNumDictNew[neighbor] -= 1
    
    checkNDN = list(numDictNew.keys())
    for b in checkNDN:
        if len(numDictNew[b]) == 0:
            del numDictNew[b]
    
    return graphDictNew, numDictNew, nodeNumDictNew

def recur(listOfDict):
    print("entering function")

    results = []

    numNodes = len(listOfDict[0])
    print("graph length:", len(listOfDict[0]))

    if numNodes <=1:
        for key in listOfDict[0].keys():
            results.append(key) 
        print("cb:", results)
        return results

    graphDict = {}
    numDict = {}
    nodeNumDict = {}

    for i in listOfDict[0].keys():

        graphDict[i] = listOfDict[0][i]

        numNodes = len(listOfDict[0][i])
        nodeNumDict[i] = numNodes

        if numNodes in numDict:
            numDict[numNodes] +=[i]
        else:
            numDict[numNodes] = [i]

    
    listOfDict = [graphDict, numDict, nodeNumDict]
    print(listOfDict)

    if 0 in numDict: #this 0 should be referring to "nodes with degree 0" and not "node 0" right
        nodesToAdd = numDict[0]
        results += nodesToAdd
        
        for i in nodesToAdd:
            listOfDict = deleteNode(listOfDict, i)

    if 1 in numDict:
        nodesToAdd = numDict[1]
        
        results += nodesToAdd #all deg 1 nodes
        
        print("nodes to add:", nodesToAdd)
        for i in nodesToAdd: # i need go delete its neighbors AND ITSELF
            neighborsToDelete = graphDict[i]
            
            for j in neighborsToDelete:
                print("j:", j)
                print("new graphs:", listOfDict[0])
                if j in listOfDict[0]:
                    listOfDict = deleteNode(listOfDict, j)
                    print("check for num dict:", listOfDict)
            
            print("og fella:", i)
            if i in listOfDict[0]:
                listOfDict = deleteNode(listOfDict, i)

    print("intermediate results:", results)
    print(listOfDict)

    if len(listOfDict[0]) == 0:
        return results

    if max(listOfDict[1]) > 2: #my recursion line
        #excluding case

        print(listOfDict[1])
        nodeToDelete = listOfDict[1][max(listOfDict[1])][0]
        print("node to delete:", nodeToDelete)
        nodeToDeleteNeighbours = listOfDict[0][nodeToDelete]
        print("neighbours:", nodeToDeleteNeighbours)
        revisedListExcl = deleteNode(listOfDict, nodeToDelete)
        print("revised:", revisedListExcl)
        excl_case = recur(revisedListExcl)
        for i in nodeToDeleteNeighbours:
            revisedListIncl = deleteNode(listOfDict, i)
        incl_case = recur(revisedListIncl)

        if excl_case == None:
            excl_case = []
        if incl_case == None:
            incl_case = []

        print(excl_case, type(excl_case), incl_case, type(incl_case))
        if len(excl_case) >= len(incl_case):
            print("1. results:", results, type(results), ", excl case:", excl_case, type(excl_case))
            print("1a", results.append(excl_case))
            # return results.append(excl_case)
            results = excl_case 
            # return results
        elif len(incl_case) > len(excl_case):
            print("2. results:", results, type(results), ", incl case:", incl_case, type(incl_case))
            print("2a", results.append(incl_case))
            # return results.append(incl_case.append(nodeToDelete))
            results = incl_case.append(nodeToDelete)
            # return results
        
        

    elif 2 in listOfDict[1]: #base case 1: if all is just node 2 pick n append to return list n return
        #iterate through numDict[2] to append fellas alternatingly
        print("numDict:", listOfDict[1])
        i = 0
        while i < len(listOfDict[1][2]):
            results.append(listOfDict[1][2][i])
            i += 2
    
    print("final results:", results)
    if results == None:
        return []
    return results




graphDict = {0: [3, 4, 5], 1: [3, 4, 5], 2: [3, 4, 5], 3: [0, 1, 2], 4: [0, 1, 2], 5: [0, 1, 2]}
numDict = {3: [0, 1, 2, 3, 4, 5]}
nodeNumDict = {0: 3, 1: 3, 2: 3, 3: 3, 4: 3, 5: 3}
    
listOfDict = [graphDict, numDict, nodeNumDict]

trying = listOfDict
print(recur(trying))