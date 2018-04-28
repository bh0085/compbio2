#!/usr/bin/env python

from Bio import pairwise2
from Bio import SeqIO
from Bio.SubsMat.MatrixInfo import blosum62
from Bio.SeqIO.QualityIO import FastqGeneralIterator
from Bio.Blast.Applications import NcbiblastxCommandline

import numpy as np


reads_fq_file = "/data/compbio2/linyi/EMX1-WT.r1.consolidated.fastq"
reads_fa_file = "/data/compbio2/linyi/EMX1-WT.r1.consolidated.fasta"


def analysis1():
    seq1 = SeqIO.read("/data/compbio2/linyi/emx1.fa", "fasta")
    scores = []
    #records in the fastq file is 1385196
    scores = np.zeros(1385196)
    count = 0

    with open(reads_fa_file) as in_handle:
        for title, seq, qual in FastqGeneralIterator(in_handle):
            alignments = pairwise2.align.globalds(seq1.seq, seq, blosum62, -10, -0.5)
            scores[count] = alignments[0][2]
            count+=1


    return scores    

def reads2fasta():
    with open(reads_fq_file) as in_handle:
        with open(reads_fa_file,"w") as out_handle:
            count = SeqIO.convert(in_handle, "fastq" , out_handle, "fasta")
            


def analysis2():
    blastx_cline = NcbiblastxCommandline(query=reads_fa_file, db="emx1.fa", evalue=0.001,
                                         outfmt=5, out="emx1.blast.xml")
    print(blastx_cline)
    stdout, stderr = blastx_cline()


def render():
    scores = linyi.analysis1()
    text = "First 10 scores: \n{0}".format("\n".join([str(e) for e in scores[:10]]))
        
    
if __name__=="__main__":
    print( analysis2() )
