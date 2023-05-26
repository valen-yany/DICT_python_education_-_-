LIST_IGNORE = []
output = 0


def string_similarity(reg_string, string, index_1=0, index_2=0, output=False, one=False):

    if index_1 == len(reg_string) or index_2 == len(string):
        return output

    output = check_similarity(reg_string[index_1], string[index_2], index_1)

    if len(reg_string) > index_1+1 and reg_string[index_1 + 1] == '?' and index_1+1 not in LIST_IGNORE:
        return string_similarity(reg_string[:index_1 + 1] + reg_string[index_1 + 2:], string, index_1, index_2, output, one) if output \
            else string_similarity(reg_string[:index_1] + reg_string[index_1 + 2:], string, index_1, index_2, output, one)

    if len(reg_string) > index_1+1 and reg_string[index_1 + 1] == '*' and index_1+1 not in LIST_IGNORE:
        return string_similarity(reg_string, string, index_1, index_2 + 1, output, one) if output \
            else string_similarity(reg_string[:index_1] + reg_string[index_1 + 2:], string, index_1, index_2, output, one)

    if len(reg_string) > index_1+1 and reg_string[index_1 + 1] == '+' and index_1+1 not in LIST_IGNORE:
        if output:
            return string_similarity(reg_string, string, index_1, index_2 + 1, output, one)
        elif index_2-index_1 >= 1:
            return string_similarity(reg_string[:index_1] + reg_string[index_1 + 2:], string, index_1, index_2, output, one)
        else:
            return False

    if output:
        return string_similarity(reg_string, string, index_1 + 1, index_2 + 1, output, one)
    elif one:
        return False
    else:
        return string_similarity(reg_string, string, 0, index_2 - index_1 + 1, output, one)


def set_start_end(reg_string, string):
    operation = 0

    if reg_string.startswith('^') and 0 not in LIST_IGNORE:
        operation += 1
        reg_string = reg_string[1:]

    if reg_string.endswith('$') and len(reg_string) - 1 not in LIST_IGNORE:
        operation += 2
        reg_string = reg_string[:-1]

    if operation == 0:
        return string_similarity(reg_string, string)
    elif operation == 1:
        return string_similarity(reg_string, string, 0, 0, False, True)
    elif operation == 2:
        return string_similarity(reg_string[::-1], string[::-1], 0, 0, False, True)
    elif operation == 3:
        return string_similarity(reg_string, string, 0, 0, False, True) and string_similarity(reg_string[::-1], string[::-1], 0, 0, False,
                                                                                              True)


def get_ignore(str1):
    result = ""
    for i, char in enumerate(str1):
        if char == '\\' and i - len(LIST_IGNORE) not in LIST_IGNORE:
            LIST_IGNORE.append(i - len(LIST_IGNORE))
        else:
            result += char
    return result


def check_similarity(symbol1, symbol2, index1=0):

    if symbol1 == symbol2 or (symbol1 == '.' and index1 not in LIST_IGNORE):
        return True
    elif not symbol1 and symbol2:
        return True
    elif not symbol1 and not symbol2:
        return True
    elif symbol1 and not symbol2:
        return False
    return False


while True:
    LIST_IGNORE.clear()
    input_string = input()
    if input_string == 'quit':
        break
    if '|' not in input_string:
        continue
    splitted_string = input_string.split('|')
    transform_str = get_ignore(splitted_string[0])
    output = set_start_end(transform_str, splitted_string[1])

    print(f"input: '{input_string}'  result: {output}")
