from os import system,name


# CLEARS CLI WINDOW
def clear():
    system('cls' if name == 'nt' else 'clear')


# SORT A LIST WITHIN A LIST BASED ON CONTENT OF INDEX OF INNER LIST
def sort_list_in_list(index:int, list_of_list_to_be_sorted=None):
    return sorted(list_of_list_to_be_sorted, key=lambda x: x[index])