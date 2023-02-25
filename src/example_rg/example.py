import ast


def string_to_list(string: str) -> list:
    return ast.literal_eval(string)
