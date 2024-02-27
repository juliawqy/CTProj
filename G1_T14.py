def Invitees(g: Graph):
    '''
      return list "results" # including the list of node index recommended
      e.g., results = [0, 1] denotes that friends 0 and 1 will be invited
    '''
    results = []
    # do not change the code above

    # ******************** implement your code here ***********************
   
    #################
    # FINAL VERSION #
    #################
    
    
    totalFriends = g.getNodeNum()  
    
    ###########################################################
    # Only does the greedy if the number of nodes more than 1 #
    ###########################################################
    
    if totalFriends >0:

        if(g.getJobNum()<3):
            return []

        candidate_list_num = {}
        for i in range(totalFriends):
            candidate_list_num[i] = g.getDegree(i)

        candidate_list_num = {k: v for k, v in sorted(candidate_list_num.items(), key=lambda item: item[1])}  #sorts the dict in ascending degree order 
           
        ##############################################################
        # Add in the first 3 unique jobs based on lowest degree node #
        ##############################################################
        
        
        jobs_inputted = []
        nodes_to_not_visit = []
        
        if (g.getJobNum()>=3):

            temp1 = list(candidate_list_num.keys()) #freezes a list of nodes for the 'for loop' to iterate through

            for node in temp1:
                if node not in nodes_to_not_visit:
                    nodes_to_not_visit += [node]

                    job = g.getJobs(node)

                    if job not in jobs_inputted:                   
                        results += [node]
                        jobs_inputted += [job]

                        deg = candidate_list_num[node]
                        for j in range(deg):
                            neighbor = g.getEdge(node, j)
                            if neighbor in candidate_list_num:
                                nodes_to_not_visit += [neighbor]
                                del candidate_list_num[neighbor]             
                        del candidate_list_num[node]

                if jobs_inputted == 3:
                    break
        
        
        ######################################################################
        # THIS IS THE PART THAT RETURNS AN EMPTY LIST IF CNT MIS WITH 3 JOBS #
        ######################################################################
        
        
        if len(jobs_inputted)<3:
            return []
       
    
        #####################################################################################################################
        # Greedy based on the lowest edges, no matter the job --> goal is to get as many people as possible so lowest first #
        #####################################################################################################################

        
        while len(list(candidate_list_num.keys())) > 0:                  
            results.append(list(candidate_list_num.keys())[0])

            appended = list(candidate_list_num.keys())[0]
            degAppended = candidate_list_num[appended]

            for i in range(degAppended):
                neighbor = g.getEdge(appended, i)

                if neighbor in candidate_list_num:
                    del candidate_list_num[neighbor]

            del candidate_list_num[appended]
            
            
    # *********************************************************************

    # do not change the code below
    return results
