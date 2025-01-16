from datetime import date
import pandas as pd
import streamlit as st


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
            return difference
        else:
            st.warning("A data de check-out deve ser posterior à data de check-in.")
            return 0
    else:
        st.warning(f"As entradas não são do tipo `date`")
        return 0



def brazil_datestr(year_first_date: str | date) -> str:
    """Converts a date like object to Brazilian date format (DD/MM/YYY)
    
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
        print(f"Error trying to convert: {e}")
        return year_first_date


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
        print("Input must be a Pandas DataFrame.")
        return None
    df_new = df.copy()
    date_columns = ['checkin', 'checkout', 'criado_em', 'modificado_em', 'data_pagamento']
    for col in df_new.columns:
        if col in date_columns:
            try:
                if isinstance(df_new[col].iloc[0], date):
                    df_new[col] = df_new[col].apply(lambda x: x.strftime('%d/%m/%Y') if isinstance(x, date) else x)
                else:
                    df_new[col] = pd.to_datetime(df_new[col], errors='coerce').dt.strftime('%d/%m/%Y')
            except (ValueError, TypeError) as e:
                print(f"Warning: Column '{col}' could not be converted to date: {e}")
                pass
    return df_new


def str_to_date(str_date: str) -> date:
    try:
        date_date = pd.to_datetime(arg=str_date, yearfirst=True).date()
    except (ValueError, AttributeError):
        date_date = None
        return str_date
    return date_date