from datetime import date, timedelta
import pandas as pd
import requests
import streamlit as st


def brazil_datestr(year_first_date: str | date) -> str:
    """Converts a date like object to Brazilian date format (DD/MM/YYYY)

    Args:
        year_first_date: The input of a date like object, normally starts with Year

    Returns:
        A new Brazilian date like string.
        If fails, returns the same input.
    """
    try:
        br_date = pd.to_datetime(year_first_date).strftime("%d/%m/%Y")
        return br_date
    except Exception as e:
        st.error(f"Error trying to convert: {e}")
        return year_first_date


def calculate_diarias(checkin, checkout):
    """Calculates in days the difference between checkout and checkin.

    Args:
        checkin: date
        checkout: date

    Returns:
        An integer number equals the difference.
        `0` if inputs are not `date` types.
        `0` if `difference < 1`.
    """
    if isinstance(checkin, date) and isinstance(checkout, date):
        difference = (checkout - checkin).days
        if difference >= 1:
            st.write(f"Diarias: {difference} dias")
            return difference
        else:
            st.warning("A data de check-out deve ser posterior à data de check-in.")
            st.write(f"Diarias: 0 dias")
            return 0
    else:
        st.warning(f"Insira as datas de Check-in e Check-out")
        st.write(f"Diarias: 0 dias")
        return 0


def gen_reserv_table(year, month):
    first_day = date(year, month, 1)
    last_day = (
        date(year, month + 1, 1) - timedelta(days=1)
        if month < 12
        else date(year + 1, 1, 1) - timedelta(days=1)
    )
    get_aptos = requests.get("http://api:8000/apartamentos/")
    get_alugueis = requests.get("http://api:8000/alugueis/")
    aptos = get_aptos.json()
    alugueis = get_alugueis.json()
    df_alugueis = pd.DataFrame(alugueis, columns=["apto_id", "checkin", "checkout"])
    df_aptos = pd.DataFrame(aptos, columns=["id"])
    month_days = (first_day - last_day).days + 1
    table_days = [first_day + timedelta(days=1) for i in range(month_days)]
    df_table = pd.DataFrame(index=df_aptos["id"].unique(), columns=table_days)
    for _, aluguel in df_alugueis.iterrows():
        checkin = aluguel["checkin"]
        checkout = aluguel["checkout"]
        apto = aluguel["apto_id"]
        for day in table_days:
            if day == checkin:
                df_table.loc[apto, day] = "//"
            elif day == checkout - timedelta(days=1):
                df_table.loc[apto, day] = "(/)"
            else:
                df_table.loc[apto, day] = "/"  ## Talvez o nome ou valores

    return df_table


def showbr_dfdate(df: pd.DataFrame) -> pd.DataFrame:
    """Converts specific DataFrame columns containing datetime.date objects to
    Brazilian date format (DD/MM/YYYY).

    Args:
        df: The input DataFrame.

    Returns:
        A new DataFrame with converted date columns, or the original DataFrame
        if no conversions were possible. Only columns specified for this project are converted.
        Returns None if input is not a DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        st.warning("Input must be a Pandas DataFrame.")
        return None
    df_new = df.copy()
    date_columns = [
        "checkin",
        "checkout",
        "criado_em",
        "modificado_em",
        "data_pagamento",
    ]
    for col in df_new.columns:
        if col in date_columns:
            try:
                if isinstance(df_new[col].iloc[0], date):
                    df_new[col] = df_new[col].apply(
                        lambda x: x.strftime("%d/%m/%Y") if isinstance(x, date) else x
                    )
                else:
                    df_new[col] = pd.to_datetime(
                        df_new[col], errors="coerce"
                    ).dt.strftime("%d/%m/%Y")
            except (ValueError, TypeError) as e:
                st.warning(
                    f"Warning: Column '{col}' could not be converted to date: {e}"
                )
                pass
    return df_new


def str_to_date(str_date: str) -> date:
    try:
        date_date = pd.to_datetime(arg=str_date, yearfirst=True, dayfirst=True).date()
    except (ValueError, AttributeError):
        date_date = None
        return str_date
    return date_date
