def empty_none_dict(obj: dict) -> dict:
    if type(obj) == dict:
        for k, v in obj.items():
            if v is None:
                obj[k] = None
            elif isinstance(v, str):
                if (v.strip() == '' or 
                    v.strip() == 'None' or 
                    v.strip() == 'null'):
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
    if value == None:
        return None
    else:
        return str(value)