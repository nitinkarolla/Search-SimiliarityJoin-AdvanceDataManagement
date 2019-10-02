#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
"""
    Main file
"""
import csv
from simJoin import SimilarityJoinED

"""
    Supplement function ReadDataFromFile()
"""
def ReadDataFromFile(filepath):
    with open(filename) as f:
        content = f.readlines()
    dat = [x.strip() for x in content]
    return dat

"""
    Supplement function WriteResults()
    Write list of list into disk as a csv file
"""
def WriteResults(dat):
    with open("out_4_pass.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(dat)


if __name__ == "__main__":
    filename = "E:/Semester-3/Advance Data Management/Search-SimiliarityJoin-AdvanceDataManagement/testset/sample_test3.txt"		## Input file path (Can be modified while you are testing code)
    edtau = 2		## Threshold:tau (Can be modified while you are testing code)

    dat = ReadDataFromFile(filename)

    start_time = time.time()
    
    output = SimilarityJoinED(dat,edtau)
    #print(output)
    WriteResults(output)
    print("--- %s seconds ---" % (time.time() - start_time))
       
    ## Test Case1: Check number of matched pairs (In bash)
    ## Manually run `wc -l answer.csv` & `wc -l out.csv` to check if number matches.

    ## Test Case2: Validate the output using `diff` (In bash)
    ## diff -y --suppress-common-lines answer.csv out.csv | grep '^' | wc -l

    ## Note for `diff`: Since different OS use different symbol for newline, for your own testing phase,
    ##                  you might want to use `dos2unix` to transfer windows newlines into unix type before using `diff`

