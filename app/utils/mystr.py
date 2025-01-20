import numpy as np
import pandas as pd
import streamlit as st

def csv_handler(csv):
    if csv is not None:
        try:
            df = pd.read_csv(
                csv,
                dtype=str,
                encoding='utf-8-sig',
                header=0
            )
            df = df.replace('', None)
            df = df.replace({pd.NA: None, np.nan: None})
            df.columns = [
                'Timestamp','nome','cidade','cep','uf','pais','tel','estado_civil','profissao','rg','cpf','mae','checkin','checkout','automovel','modelo_auto','placa_auto','cor_auto',
                'a0_nome','a0_doc','a0_idade','a0_parentesco',
                'a1_nome','a1_doc','a1_idade','a1_parentesco',
                'a2_nome','a2_doc','a2_idade','a2_parentesco',
                'a3_nome','a3_doc','a3_idade','a3_parentesco',
                'a4_nome','a4_doc','a4_idade','a4_parentesco',
                'a5_nome','a5_doc','a5_idade','a5_parentesco',
                'a6_nome','a6_doc','a6_idade','a6_parentesco',
                'a7_nome','a7_doc','a7_idade','a7_parentesco',
                'a8_nome','a8_doc','a8_idade','a8_parentesco',
                'a9_nome','a9_doc','a9_idade','a9_parentesco',
            ]
            return df
        except pd.errors.ParserError:
            st.error("Erro: O arquivo enviado não é um CSV válido ou está mal formatado.")
        except Exception as e:
            st.error(f"Ocorreu um erro ao processar o arquivo: {e}")


def empty_none_dict(obj: dict) -> dict:
    if type(obj) == dict:
        for k, v in obj.items():
            if v is None:
                obj[k] = None
            elif isinstance(v, str):
                if (v.strip() == '' or 
                    v.strip().upper() == 'NONE' or 
                    v.strip().upper() == 'NULL' or
                    v.strip().upper() == 'NAN' or
                    v.strip().upper() == 'NA'
                ):
                    obj[k] = None
    return obj


def format_apto(input: str) -> str:
    """Formats a string to 'letter-number'.
    Args:
        input: string to be formated.
    Returns:
        Desired format string.
    """
    numbers = ""
    letter = ""
    for c in input:
        if c.isdigit():
            numbers += c
        else:
            letter = c
    return f'{letter.upper()}-{numbers}'


def none_or_str(value: str | None) -> str | None:
    if value:
        if value == None:
            return None
        else:
            return str(value)
    else:
        return None
    

def two_liner(s: str):
    if len(s) > 77:
        s = s.split(' ')
        s1 =[]
        s2 = s.copy()
        for i in range(0, len(s)-1):
            s1.append(s[i])
            del s2[0]
            if len(' '.join(s1)) > 77:
                s1.pop()
                s2.insert(0, s[i])
                break
        l1 = ' '.join(s1)
        l2 = ' '.join(s2)
        return l1, l2
    else:
        return s
