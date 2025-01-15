from datetime import date
import json
import pandas as pd
import re
import requests
import streamlit as st


def format_input_for_db(input: str, output: str = 'str'):
    """
    Formats an input string for database storage.

    Args:
        input_str: str
            The input string from a form.
        output: str, optional
            The desired output type. 
            Supported types: 
                - 'str' (default): Returns the input string after basic cleaning.
                - 'int': Attempts to convert the input to an integer.
                - 'float': Attempts to convert the input to a float.
                - 'date': Attempts to convert the input to a datetime.date object. 
                - 'none': Returns None if the input is empty.

    Returns:
        str | int | float | date | None
            The formatted value according to the specified output type.

    Raises:
        ValueError: If the input string cannot be converted to the specified output type.

    Example:
        format_input("123", "int")  # Returns 123
        format_input("3.14", "float")  # Returns 3.14
        format_input("2023-12-25", "date")  # Returns datetime.date(2023, 12, 25) 
        format_input("", "str")  # Returns ""
        format_input("", "none")  # Returns None
    """

    if input == None:
        match output:
            case 'none':
                return None
            case 'str':
                return ' '
            case 'int':
                return 0
            case 'float':
                return 0.0
            case 'date':
                return date(2025, 1, 1)
    else:
        match output:
            case 'none':
                return None
            case 'str':
                return re.sub(r'\s+', ' ', input).strip()

            


    
    
    
    
    # chars = r"[+\(\)\-\,\.\'\"\@\#\$\%\¨\&\*\!\?\;\:\<\>\~\^\]\[\{\}\=\_\ ]"
    # clean = re.sub(chars, '', input)
    # return clean


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


## Criando a função para a tab de update
def update_fields_creator(update_id: int, table: str, reg: str, page_n: int):
    response = requests.get(f'http://backend:8000/{table}/{update_id}')
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
            unique_key = f"{page_n}_{k}_{i}"
            v = st.text_input(
                label=k,
                key=unique_key,
                value=v
            )
            updated[k] = v
        update_button = st.form_submit_button('Modificar')
        if update_button:
            updated_json = json.dumps(obj=updated, indent=1, separators=(',',':'))
            response = requests.put(f"http://backend:8000/{table}/{update_id}", data=updated_json)
            show_response_message(response)


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
