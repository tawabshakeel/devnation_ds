def string_case(char_list):
    return list(set(map(convert_low_up, char_list)))
def convert_low_up(x):
    return x.lower(), x.upper()