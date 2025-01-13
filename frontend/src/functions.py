
import pandas as pd
import re
import streamlit as st


def clean_number(input):
    """Remove caracteres especiais de um texto.
    Args:
        texto: O texto a ser limpo.
    Returns:
        O texto com os caracteres especiais removidos.
    """
    chars = r"[+\(\)\-\,\.\'\"\@\#\$\%\¨\&\*\!\?\;\:\<\>\~\^\]\[\{\}\=\_\ ]"
    clean = re.sub(chars, '', input)
    return clean


def convert_empty_to_none():
    """Converts global empty strings to None."""
    global_vars = globals().copy()
    for var_name, var_value in global_vars.items():
        if var_name.startswith("__") or callable(var_value) or isinstance(var_value, type(convert_empty_to_none)):
            continue
        if isinstance(var_value, str) and var_value == "":
            globals()[var_name] = None


def none_or_str(value: str | None) -> str | None:
    if value == None:
        return None
    else:
        return str(value)


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


def string_to_date(str_date: str) -> date:
    try:
        date_date = pd.to_datetime(str_date).date()
    except (ValueError, AttributeError):
        date_date = None
    return date_date
