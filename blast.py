import settings
from utils import get_records, download_protein_sequences_from_ncbi
import subprocess 

def blast():
    print("Checking if blast+ is installed ...")
    result = subprocess.run("sh blast_download.sh", shell=True, capture_output=True, text=True)
    result = result.stdout
    print(result)
    if "ncbi blast+ is installed." not in result:
        return False

    protein_name = input("Provide the protein symbol: ").strip()
    reference_acc = input("Provide the protein reference accession number: ").strip()
    isolate_protein_fasta_file = f"{settings.OUTPUT_DATA_DIRECTORY_PATH}{protein_name}_{reference_acc}_isolate_protein.fasta"
    ref_protein_fasta_file = f"{settings.OUTPUT_DATA_DIRECTORY_PATH}{reference_acc}_ref_protein.fasta"

    if settings.UPDATE:
        print("Preparing microbiggie id file ...")
        microbigge_inp_file = f"{settings.OUTPUT_DATA_DIRECTORY_PATH}{settings.MICROBIGGE_FILENAME}"
        microbigge_out_file = f"{settings.OUTPUT_DATA_DIRECTORY_PATH}{settings.MICROBIGGE_OUTPUT_FILENAME}"
        get_records(microbigge_inp_file, microbigge_out_file)
        download_protein_sequences_from_ncbi(microbigge_out_file, isolate_protein_fasta_file, ref_protein_fasta_file,  protein_name, reference_acc, settings.EMAIL)
    else:
        print("All neccessary files are already available ...")

    blast_output_file = f"{settings.OUTPUT_DATA_DIRECTORY_PATH}{protein_name}_{reference_acc}_blastp_output"
    
    print("Running blastp ...")
    subprocess.run("sh blastp.sh", shell=True, env={"QUERY_FILE": isolate_protein_fasta_file, "SUBJECT_FILE": ref_protein_fasta_file, "OUT_FILE": blast_output_file})
    print("blastp has finished running ...")
blast()