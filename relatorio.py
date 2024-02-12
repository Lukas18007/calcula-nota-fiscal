import csv

def create_csv_from_nfs(nfs_values):
    with open('nfs.csv', 'w', newline='') as csvfile:
        fieldnames = ['valor_servico', 'data_emissao']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for nfs in nfs_values:
            writer.writerow(nfs)

        return True