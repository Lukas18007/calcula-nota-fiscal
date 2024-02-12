from PyPDF2 import PdfReader
import os
import re

def get_nf_values():
    nfs = []

    for _, _, arquivos in os.walk('./NFS'):
        for arquivo in arquivos:
            if arquivo.endswith('.pdf'):
                with open(f'./NFS/{arquivo}', 'rb') as arquivo:
                    pdf = PdfReader(arquivo)
                    num_paginas = len(pdf.pages)
                    for i in range(0, num_paginas):
                        page = pdf.pages[i]
                        texto = page.extract_text()

                        valor_servico = re.findall(r"[1-9]\d{0,2}(?:\.\d{3})*,\d{2}", texto)[0]
                        data = re.findall(r"(?<!\d)(\d{2})/(?<!\d)(\d{2})/(?<!\d)(\d{4})(?!\d)", texto)[0]

                        mes = data[1]
                        ano = data[2]
                        data_emissao = f'{mes}/{ano}'

                        nfs.append({
                            'valor_servico': valor_servico,
                            'data_emissao': data_emissao
                        })
                        
        return nfs