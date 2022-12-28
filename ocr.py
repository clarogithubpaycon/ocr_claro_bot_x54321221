import os
import streamlit as st
from json import loads
import pandas as pd
from FuncsForSPO.fpdf.focr.orc import faz_ocr_em_pdf
from FuncsForSPO.fpython.functions_for_py import arquivos_com_caminho_absoluto_do_arquivo




st.markdown("""
# OCR

### Envie um PDF e aguarde o OCR dele...
            
            """)

arquivo = st.file_uploader("Envie seu PDF aqui!", type=['pdf'])

if arquivo:
    print(arquivo.type)
    print(arquivo)
    print(arquivo)
    match arquivo.type.split('/'):
        case 'application', 'pdf':
            action = st.button('Execute o OCR...')
            
            if action:
                bytes_data = arquivo.getvalue()
                with open('pdf.pdf', 'wb') as b:
                    b.write(bytes_data)
                st.warning('Aguarde a API de OCR...')
                try:
                    text = faz_ocr_em_pdf('pdf.pdf')
                except Exception:
                    text = arquivos_com_caminho_absoluto_do_arquivo('tempdir')
                st.success('Texto recuperado com sucesso!')
                st.text(text)
                os.remove('pdf.pdf')
else:
    st.error('Ainda não tenho arquivo...')
