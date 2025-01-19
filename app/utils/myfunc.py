import json
import pandas as pd
import requests
import streamlit as st
from typing import List


def cat_index(df: pd.DataFrame, label: str, cats: List[str]):
    for i in range(0, len(cats)):
        if df.loc[0, label] == cats[i]:
            return i


def merge_dictionaries(dict1_data, dict2_data):
  """
  Merges two dictionaries into a single dictionary.

  Args:
    dic1_data: Dictionary containing data.
    dict2_data: Dictionary containing data.

  Returns:
    A dictionary with merged data.
  """
  merged_data = {**dict1_data, **dict2_data} 
  return merged_data


def show_data_output(data: dict):
    if isinstance(data, dict):
        df = pd.DataFrame([data])
        if 'id' in df.columns:
            st.dataframe(df.set_index('id'))
        else:
            st.dataframe(df, hide_index=True)


def show_response_message(response) -> None:
    if response.status_code == 200:
        st.success('Operação realizada com sucesso!')
    else:
        try:
            data = response.json()
            if 'detail' in data:
                if isinstance(data['detail'], list):
                    errors = '\n'.join([error['msg'] for error in data['detail']])
                    st.error(f'Erro: {errors}')
                else:
                    st.error(f'Erro: {data["detail"]}')
        except ValueError:
            st.error('Erro desconhecido. Não foi possível decodificar a resposta.')


def update_fields_generator(id: int, table: str, reg: str, page_n: int):
    response = requests.get(f'http://backend:8000/{table}/{id}')
    if response.status_code == 200:
        reg_viz = response.json()
        df = pd.DataFrame([reg_viz])
        st.dataframe(df, hide_index=True)
    else:
        show_response_message(response)
        return
    ignored_columns = {'id', 'criado_em', 'modificado_em'}
    with st.form(f'update_{reg}'):
        updated = {}
        for i, (k, v) in enumerate(df.iloc[0].items()):
            if k in ignored_columns:
                continue
            unique_key = f"{page_n}_{k}_{i}_up"
            v = st.text_input(
                label=k,
                key=unique_key,
                value=v
            )
            updated[k] = v
        update_button = st.form_submit_button('Modificar')
        if update_button:
            updated_json = json.dumps(obj=updated, indent=1, separators=(',',':'))
            response = requests.put(f"http://backend:8000/{table}/{id}", data=updated_json)
            show_response_message(response)
