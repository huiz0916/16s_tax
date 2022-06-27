from Bio import Entrez, SeqIO
from Bio.Blast import NCBIWWW, Record, NCBIXML





result_handle = open("test_my_blast.xml", "r")
blast_records = NCBIXML.read(result_handle)

E_VALUE_THRESH = 0.04
#print("qaccver saccver pident length mismatch gapopen qstart qend sstart send evalue bitscore qcovs")
gi_id_list = []
for alignment in blast_records.alignments:
    gi_id = alignment.title.split("|")[1]
    #print(type(gi_id))
    gi_id_list.append(gi_id)

search_results = Entrez.read(Entrez.epost("pubmed", id=",".join(gi_id_list)[0:2]))

    
    #for hsp in alignment.hsps:
    #    print('sequence:', alignment.length)



result_handle.close()

