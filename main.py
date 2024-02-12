from nf import get_nf_values
from relatorio import create_csv_from_nfs

nfs_values = get_nf_values()

if nfs_values:
    if create_csv_from_nfs(nfs_values):
        print('CSV criado com sucesso!')
    else:
        print('Erro ao criar CSV!')
else:
    print("Não foram encontradas NFs")