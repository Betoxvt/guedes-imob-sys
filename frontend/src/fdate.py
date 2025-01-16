# Date related custom functions
from datetime import date
import pandas as pd

def string_to_date(str_date: str) -> date:
    try:
        date_date = pd.to_datetime(str_date).date()
    except (ValueError, AttributeError):
        date_date = None
        return str_date
    return date_date