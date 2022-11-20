def sort_string(any_string):
    sort = ""
    for str in any_string:
        if str < any_string[0]:
            sort = any_string + sort
        else:
            sort = sort + any_string
    return sort

def is_anagram(first_string, second_string):
    string_1 = sort_string(first_string.lower())
    string_2 = sort_string(second_string.lower())
    if string_1 == "" and string_2 == "":
        return (string_1, string_2, False)
    if string_1 != string_2:
        return (string_1, string_2, False)
    if string_1 == string_2:
        return (string_1, string_2, True)