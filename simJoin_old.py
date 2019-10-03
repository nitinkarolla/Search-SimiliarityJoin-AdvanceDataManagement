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

def buildInvertedIndex(inverted_index, s, threshold, s_index, w_position):
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
            w_position[(len(s), segment)] = start
        else:
            if s[start:end] not in inverted_index[(len(s), segment)]:
                inverted_index[(len(s), segment)] [s[start:end]]= [s_index]
            else:
                inverted_index[(len(s), segment)] [s[start:end]].append(s_index)
    return inverted_index, w_position

#l1, l2 =  buildInvertedIndex({}, 'hellasdefgweas', 2, 1, {})

def subStringSelection(s,index):
    """
    Simple Substring Selection
    """
    W_s_Lli = []
    #if 
    for k in index.keys():
        if k in s:
            W_s_Lli.append(k)
    return W_s_Lli

def subStringSelection2(S, s ,inverted_index, threshold, w_position,l,i):
    """
    Substring Selection - Multi-match-aware
    """
    W_s_Lli = []
    for w in inverted_index[(l,i)]:
        delta = abs(len(S[s])- l)
        p_i = w_position[(l,i)]
        start = max([p_i - i , p_i + delta - (threshold - i)])
        end = min ([p_i + i, p_i + delta + (threshold - i)]) + 1 + len(w)
        if w in S[s][start:end]:
            W_s_Lli.append((w,p_i))
    return W_s_Lli

def Verification(S,s,R,threshold):
    out = []
    for r in R:
        distance = EditDistance(S[s],S[r])
        if distance <= threshold:
            out.append((s,r, distance))
    return out

def split(s, start, end, w):
    w_start = start + s[start:end+1].find(w)
    end = w_start + len(w)
    s = [s[:w_start], s[w_start + len(w) :]] 
    return s

def Verification2(S, s_index, w, R, threshold,i, ed_dict, dat_org):
    out = []
    for r_1 in R:
        if (s_index,r_1) in ed_dict:
            continue
        else:
            ed_dict[(s_index,r_1)] = 1
        if len(S[s_index].split(w[0])) > 2:
            delta = abs(len(S[s_index])- len(S[r_1]))
            start = max([w[1] - i , w[1] + delta - (threshold - i)])
            end = min ([w[1] + i, w[1] + delta + (threshold - i)]) + 1 + len(w)
            s = split(S[s_index],start,end,w[0])
        else:
            s = S[s_index].split(w[0],1)
        r_l = S[r_1][0 : w[1]] 
        r_r = S[r_1][w[1]+ len(w[0]):]
        d1 = EditDistance(s[0], r_l)
        if d1 > i+1:
            continue
        d2 = EditDistance(s[1],r_r)
        if d1 + d2 > threshold:
            continue
        if dat_org.index(S[r_1]) < dat_org.index(S[s_index]):
            out.append((dat_org.index(S[r_1]),dat_org.index(S[s_index]), d1+d2))
        else:
            out.append((dat_org.index(S[s_index]),dat_org.index(S[r_1]), d1+d2))
        #out.append((r_1,s_index, d1+d2))
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
    dat_org = dat.copy()
    method = "" # Other options available are "Normal", "Index", "SimplePass"


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
        w_position = {}
        for s in range(len(S)):
            if s == 0:
                inverted_index , w_position = buildInvertedIndex(inverted_index, S[s], threshold, s, w_position)
            else:
                possible_index = []
                for i in list(inverted_index.keys()):
                    if i[2] in S[s]:
                        possible_index = possible_index + inverted_index[i]
                for r in set(possible_index):
                    distance = EditDistance(S[s],S[r])
                    if distance <= threshold:
                        output.append((s,r, distance))

                inverted_index , w_position = buildInvertedIndex(inverted_index, S[s], threshold, s, w_position)


    ## Simple Pass Join 
    elif method == "SimplePass":
        S = sortLengthAlphabetical(dat)
        inverted_index = {}
        w_position={}
        for s in range(len(S)):
            if s == 0:
                inverted_index = buildInvertedIndex(inverted_index, S[s], threshold, s, w_position)
            else:
                R = []
                for l in range(len(S[s])- threshold, len(S[s])+1 ):
                    for i in range(0,threshold+1):
                        if (l,i) in inverted_index:
                            W_s_Lli = subStringSelection(S[s], inverted_index)
                            for w in W_s_Lli:
                                if w in inverted_index[(l,i)]:
                                    R = R + inverted_index[(l,i)][w]
                out = Verification(S, s, set(R), threshold)
                output = output + out
                inverted_index = buildInvertedIndex(inverted_index, S[s], threshold, s, w_position)
    
    ## Pass Join with Multi aware position subselction and Extended Verification
    else:
        S = sortLengthAlphabetical(dat)
        inverted_index = {}
        w_position = {}
        ed_dict = {}
        for s in range(len(S)):
            if s == 0:
                inverted_index , w_position = buildInvertedIndex(inverted_index, S[s], threshold, s, w_position)
            else:
                for l in range(len(S[s])- threshold, len(S[s])+1 ):
                    for i in range(0,threshold+1):
                        if (l,i) in inverted_index:
                            W_s_Lli = subStringSelection2(S, s, inverted_index, threshold, w_position,l,i)
                            for w in W_s_Lli:
                                if w[0] in inverted_index[(l,i)]:
                                    out = Verification2(S, s, w, inverted_index[(l,i)][w[0]], threshold,i, ed_dict, dat_org)
                                    if out != "Reject":
                                        output = output + out
                inverted_index , w_position = buildInvertedIndex(inverted_index, S[s], threshold, s, w_position)

    print(len(output))
    output = sorted(output, key=lambda element: (element[0], element[1]))
            
    ## Don't forget to apply threshold to omit unneeded string pairs!!
    ## Note that only string pairs with edit distance no larger than the threshold will be added to results. 
    ## If the edit distance between a pair of strings is larger than the threshold, it should not be added to the result set. 
    
    return output

