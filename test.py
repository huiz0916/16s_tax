
from Bio import Entrez, SeqIO
from Bio.Blast import NCBIWWW, Record, NCBIXML

fasta_input = open("test_16s.fa","r").read()
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_input.format("fasta"),megablast=True)
save_file = open("test_16s_blast2.xml", "w")
save_file.write(result_handle.read())
save_file.close()


'''
result_handle = open("test_16s_blast2.xml", "r")
blast_records = NCBIXML.parse(result_handle)
result_handle = open("test_16s_blast.xml", "r")
blast_records = NCBIXML.parse(result_handle)
for blast_record  in blast_records:
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            print(alignment.title)
            print(hsp.identities)
            print(alignment.length)
            print(hsp.num_alignments)
            print(hsp.query_start)
            print(hsp.query_end)
            print(hsp.sbjct_start)
            print(hsp.sbjct_end)
            print(hsp.expect)
            print(hsp.score)
'''           
        


#search_results = Entrez.read(Entrez.epost("pubmed", id=",".join(gi_id_list)[0:2]))



result_handle.close()

