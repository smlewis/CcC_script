#!/usr/bin/python

'''This script parses SSBOND records and attempts to find N to N+1 disulfide bonds.'''

#expected record format:
#1isz.pdb SSBOND   2 CYS A  254    CYS A  260                          1555   1555  2.03  
#Note this is fixed width
#Note that an insertion code MAY occur, so we are processing as fixed-width

#read file (from arg?  hardcode)
filename = "all_ssbond_recs.proc.txt"
with open(filename) as f:
    for SSBOND in f:
        chain1=SSBOND[24]
        chain2=SSBOND[38]
        #print chain1, "chainspacer", chain2
        if chain1 == chain2:
            resn1=SSBOND[26:29]
            resn2=SSBOND[40:43]
            #print resn1, "resnspacer", resn2
            if resn1 == resn2:
                print SSBOND

#for each line
#is same chain?
#are resnums adjacent?
#then, print record
