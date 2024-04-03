import settings

def get_records(inp_file, out_file):
    closest_ref_accs = []
    protein_accs = []
    protein_symbols = []
    
    with open(out_file, "w") as output:
        with open(inp_file) as f:
            f.readlines(1)
            for line in f:
                record = line.rstrip()
                columns = record.split(",")
                protein_acc = columns[1]
                if not protein_acc:
                    continue

                protein_acc = protein_acc[:protein_acc.find(".")]

                ref_acc = columns[33]
                ref_acc = ref_acc[:ref_acc.find(".")]
                protein_name = columns[44]
                amr = columns[10]
                mut_type = columns[12]
                drug_class = columns[13]
                drug = columns[14]
                if protein_acc not in protein_accs and amr == "AMR":
                    output_record = f"{protein_acc}\t{ref_acc}\t{protein_name}\t{amr}\t{mut_type}\t{drug_class}\t{drug}\n"
                    if ref_acc not in closest_ref_accs:
                        closest_ref_accs.append(ref_acc)
                        protein_symbols.append(protein_name)
                    
                    protein_accs.append(protein_acc)
                    output.write(output_record)

    filename = f"{settings.OUTPUT_DATA_DIRECTORY_PATH}unique_reference_and_protein_symbol"
    with open(filename, "w") as f:
        for i in range(len(closest_ref_accs)):
            line = f"{closest_ref_accs[i]}\t{protein_symbols[i]}\n"
            f.write(line)
