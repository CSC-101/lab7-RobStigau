def str_to_float(string : str):
    try:
        new_float = float(string)
        return new_float
    except ValueError:
        return None



