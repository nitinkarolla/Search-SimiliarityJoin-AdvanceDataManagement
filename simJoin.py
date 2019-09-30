#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Implement SimilarityJoinED()
    You can add supplement function, but it is not allowed
    to modify the function name and parameters
"""

def LenghtFilter(string1,string2, threshold):
    if abs(len(string1) - len(string2)) > threshold:
        return False
    else:
        return True

def EditDistance(string1, string2):
    """
        Edit Distance for given string1 and string2
    """
    s1 = len(string1)
    s2 = len(string2)
    if s1 == 0 and s2 == 0:
        return 0
    elif s1 == 0:
        return s2
    elif s2 == 0:
        return s1

    if string1[s1-1]==string2[s2-1]: 
        return editDistance(str1,str2,m-1,n-1) 

    return 99999


def sort_lenght_alphabetical(S):
    return

def PassJoin(dat, threshold):
    return



def SimilarityJoinED(dat, threshold):
    """
        @filename: String containing the path of the File
        @threshold: tau
        
        ======> See README.md for details
    """
    #### ==== Main algorithm to calculate Edistance ====

    ## Hint:
    # 1. Index from 0 - (len(lines)-1)
    # 2. Filters: Get the candidates (e.g. length check & multi-match etc.)
    # 3. Verify the candidates (can be interleaved with 2.)
    # 4. Output format: List of list of 3 tuples [ID1, ID2, Edistance]
    
    # ...Code here...
    output = []

    for i in range(len(dat)):
        for j in range(len(dat)):
            if i == j :
                pass
            else:
                if LenghtFilter(dat[i], dat[j], threshold):
                    distance = EditDistance(dat[i],dat[j])
                    output.append((i,j, distance))
                

    
    
    ## Don't forget to apply threshold to omit unneeded string pairs!!
    ## Note that only string pairs with edit distance no larger than the threshold will be added to results. 
    ## If the edit distance between a pair of strings is larger than the threshold, it should not be added to the result set. 
    
    return output