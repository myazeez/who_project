import sys
from Bio import Entrez
import time

def download_protein_sequences_from_ncbi(filename, protein_seq_fasta_file, ref_seq_fasta_file, protein_symbol, ref_acc, email):
    # filename is the name of the tsv file downloaded from MicroBIGG-E database
    isolate_protein_ids = []

    print("Extracting records containing our protein of interest from microbigge file ...")

    with open(filename) as f:
        for line in f:
            myline = line.rstrip()
            mylist = myline.split("\t")
            if mylist[1] == ref_acc and protein_symbol == mylist[2]:
                isolate_protein_ids.append(mylist[0])
       
    if isolate_protein_ids:
        ("Downloading from NCBI ...")
        Entrez.email = email
        n = 1
        with open(protein_seq_fasta_file, "w") as f:
            for acc in isolate_protein_ids:
                print(f"Fetching sequence for Sequence {n}")
                try:
                    result = Entrez.efetch(db="protein", id=acc, rettype="fasta", retmode="text")
                    f.write(result.read())
                    time.sleep(1)
                except:
                    pass

                n += 1

        with open(ref_seq_fasta_file, "w") as f:
            result = Entrez.efetch(db="protein", id=ref_acc, rettype="fasta", retmode="text")
            f.write(result.read())

        print("Downloading completed ...")
    else:
        print("No ids with which to query NCBI protein database ...")

