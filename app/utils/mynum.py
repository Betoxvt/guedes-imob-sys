import streamlit as st
import re


def calculate_valortotal(diarias, valor_diaria):
    if diarias is None or valor_diaria is None:
        if diarias is None:
            st.warning('Insira datas de Check-in e Check-out válidas')
        if valor_diaria is None:
            st.warning('Insira o Valor da Diária')
        return None
    if not isinstance(diarias, (int, float)) or not isinstance(valor_diaria, (int, float)):
        st.warning("As diárias e o valor da diária devem ser números.")
        return 0
    if diarias <= 0:
        st.warning("O mínimo de diárias é 1.")
    if valor_diaria <= 0:
        st.warning("O valor da diária deve ser positivo.")
    valor_total = diarias * valor_diaria
    if valor_total is None:
        st.write('Valor Total: R$ 0,00')
        return None
    if valor_total:
        st.write(f'Valor Total: R$ {valor_total}')
        return valor_total
    

def calculate_saldo(total, depositado):
    if total is None or depositado is None:
        if total is None:
            st.write('Saldo: R$ 0,00')
            return None
        if total and depositado is None:
            st.write(f'Saldo: {total*-1}')
    else:
        saldo = depositado - total
        st.write(f'Saldo: {saldo}')
        return saldo


def cep_input(cep_in: str | int | float) -> str:
    cep_num = re.sub(r'[^0-9]', '', str(cep_in))
    if len(cep_num) == 8:
        return f'{cep_num[:5]}-{cep_num[5:]}'
    else:
        st.warning('Não foi identificado o padrão brasileiro')
        return cep_in


def cpf_input(cpf_in: str | int | float) -> str:
    cpf_num = re.sub(r'[^0-9]', '', str(cpf_in))
    if len(cpf_num) == 11:
        return f'{cpf_num[:3]}.{cpf_num[3:6]}.{cpf_num[6:9]}-{cpf_num[9:]}'
    else:
        st.warning('Não foi identificado o padrão brasileiro')
        return cpf_in
    

def rg_input(rg_in: str | int | float) -> str:
    rg_num = re.sub(r'[^0-9]', '', str(rg_in))
    match len(rg_num):
        case 7:
            return f'{rg_num[:1]}.{rg_num[1:4]}.{rg_num[4:]}'
        case 8:
            if str(rg_in)[:2].isalpha():
                return f'{rg_in[:2].upper()}-{rg_num[:2]}.{rg_num[2:5]}.{rg_num[5:]}'
            if len(str(rg_in)) > 8 and str(rg_in)[8:].isalpha():
                return f'{rg_num[:2]}.{rg_num[2:5]}.{rg_num[5:]}-{rg_in[8:10].upper()}'
            else:
                return f'{rg_num[0]}.{rg_num[1:4]}.{rg_num[4:7]}-{rg_num[7]}'
        case 9:
            return f'{rg_num[:2]}.{rg_num[2:5]}.{rg_num[5:8]-[8]}'
        case 11:
            return f'{rg_num[:11]}-{rg_num[11]}'
        case _:
            st.warning('Não foi identificado o padrão brasileiro')
            return rg_in


def tel_input_br(tel_in: str | int | float) -> str:
    tel_num = re.sub(r'[^0-9]', '', str(tel_in))
    match len(tel_num):
        case 8:
            return f'{tel_num[:4]}-{tel_num[4:]}'
        case 9:
            return f'{tel_num[0]} {tel_num[1:5]}-{tel_num[5:]}'
        case 10:
            return f'+55 ({tel_num[:2]}) {tel_num[2:6]}-{tel_num[6:]}'
        case 11:
            return f'+55 ({tel_num[:2]}) {tel_num[2]} {tel_num[3:7]}-{tel_num[7:]}'
        case 12:
            return tel_num
        case 13:
            return f'+{tel_num[:2]} ({tel_num[2:4]}) {tel_num[4]} {tel_num[5:9]}-{tel_num[9:]}'
        case _:
            st.warning('Não foi identificado o padrão brasileiro')
            return tel_in


