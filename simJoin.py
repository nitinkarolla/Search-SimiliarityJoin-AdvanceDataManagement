#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

"""
    Implement SimilarityJoinED()
    You can add supplement function, but it is not allowed
    to modify the function name and parameters
"""

def EditDistance(string1, string2):
    """
        Edit Distance for given string1 and string2
    """
    if len(string1) > len(string2):
        string1, string2 = string2, string1
    distances = range(len(string1) + 1)
    for index2, char2 in enumerate(string2):
        newDistances = [index2 + 1]
        for index1, char1 in enumerate(string1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                                             distances[index1 + 1],
                                             newDistances[-1])))
        distances = newDistances
    return distances[-1]

def sortLengthAlphabetical(S):
    """
    Sorting the data first by Length and then alphabatically
    """
    S.sort(key=lambda item: (len(item), item))
    return S

def buildInvertedIndex(inverted_index, s, threshold, s_index):
    """
    Building an inverted index for given string s and threshold by spliting it into segments.
    """
    k = len(s) - math.floor(len(s)/ (threshold + 1)) * (threshold + 1)
    start = 0
    end = 0
    initial_length = math.floor(len(s)/ (threshold + 1))
    later_length = math.ceil(len(s)/ (threshold + 1))
    for segment in range(threshold + 1):
        if segment < threshold + 1 - k:
            start = end
            end = end + initial_length
        else:
            start = end
            end = end + later_length
        if (len(s), segment) not in inverted_index:
            inverted_index[(len(s), segment)] = {s[start:end] : [s_index]}
        else:
            if s[start:end] not in inverted_index[(len(s), segment)]:
                inverted_index[(len(s), segment)] [s[start:end]]= [s_index]
            else:
                inverted_index[(len(s), segment)] [s[start:end]].append(s_index)
    return inverted_index

#buildInvertedIndex({}, 'hell', 2, 1)

def subStringSelection(s,index):
    W_s_Lli = []
    for k in index.keys():
        if k in s:
            W_s_Lli.append(k)
    return W_s_Lli

def Verification(S,s,R,threshold):
    out = []
    for r in R:
        distance = EditDistance(S[s],S[r])
        if distance <= threshold:
            out.append((s,r, distance))
    return out

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
    method = "" # Other options available are "Normal", "Index"

    ## Normal Edit Distance
    if method == 'Normal':
        for i in range(len(dat)):
            for j in range(i+1,len(dat)):
                if i == j :
                    pass
                else:
                    distance = EditDistance(dat[i],dat[j])
                    if distance <= threshold:
                        output.append((i,j, distance))


    ## Inverted Index based Edit Distance
    elif method == 'Index':
        S = sortLengthAlphabetical(dat)
        inverted_index = {}
        for s in range(len(S)):
            if s == 0:
                inverted_index = buildInvertedIndex(inverted_index, S[s], threshold, s)
            else:
                possible_index = []
                for i in list(inverted_index.keys()):
                    if i[2] in S[s]:
                        possible_index = possible_index + inverted_index[i]
                for r in set(possible_index):
                    distance = EditDistance(S[s],S[r])
                    if distance <= threshold:
                        output.append((s,r, distance))

                inverted_index = buildInvertedIndex(inverted_index, S[s], threshold, s)


    ### Pass Join 
    else:
        S = sortLengthAlphabetical(dat)
        inverted_index = {}
        for s in range(len(S)):
            if s == 0:
                inverted_index = buildInvertedIndex(inverted_index, S[s], threshold, s)
            else:
                R = []
                for l in range(len(S[s])- threshold, len(S[s])+1 ):
                    for i in range(0,threshold+1):
                        if (l,i) in inverted_index:
                            W_s_Lli = subStringSelection(S[s], inverted_index[(l, i)])
                            for w in W_s_Lli:
                                if w in inverted_index[(l,i)]:
                                    R = R + inverted_index[(l,i)][w]
                out = Verification(S, s, set(R), threshold)
                output = output + out
                inverted_index = buildInvertedIndex(inverted_index, S[s], threshold, s)

    print(len(output))
            
            
    ## Don't forget to apply threshold to omit unneeded string pairs!!
    ## Note that only string pairs with edit distance no larger than the threshold will be added to results. 
    ## If the edit distance between a pair of strings is larger than the threshold, it should not be added to the result set. 
    
    return output


