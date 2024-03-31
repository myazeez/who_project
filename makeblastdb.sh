#!/bin/bash

export PATH=$PATH:/home/azeez/ncbi-blast-2.15.0+/bin
echo $FASTA_FILE
makeblastdb -in $FASTA_FILE -parse_seqids -blastdb_version 5 -taxid_map test_map.txt -title 'Cookbook demo' -dbtype prot
