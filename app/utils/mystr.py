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
