#!/usr/bin/env python

from Bio import pairwise2
from Bio import SeqIO
from Bio.SubsMat.MatrixInfo import blosum62
from Bio.SeqIO.QualityIO import FastqGeneralIterator
import numpy as np


def analysis1():

    seq1 = SeqIO.read("/data/compbio2/emx1.fa", "fasta")

    
    scores = []


    #records in the fastq file is 1385196
    scores = np.zeros(1385196)
    count = 0

    with open("/data/compbio2/EMX1-WT.r1.consolidated.fastq") as in_handle:
        for title, seq, qual in FastqGeneralIterator(in_handle):
            alignments = pairwise2.align.globalds(seq1.seq, seq, blosum62, -10, -0.5)
            scores[count] = alignments[0][2]
            count+=1

            if count > 2 :
                break

    return scores    
            


if __name__=="__main__":
    print( analysis1() )
