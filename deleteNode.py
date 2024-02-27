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