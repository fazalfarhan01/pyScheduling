from os import system, name
import io


# CLEARS CLI WINDOW
def clear():
    system('cls' if name == 'nt' else 'clear')


# SORT A LIST WITHIN A LIST BASED ON CONTENT OF INDEX OF INNER LIST
def sort_list_in_list(index: int, list_of_list_to_be_sorted=None):
    return sorted(list_of_list_to_be_sorted, key=lambda x: x[index])


# STORE CONTENT TO FILE AND PRINT
def custom_print(store_to_file, data_to_print):
    if store_to_file:
        with io.open("./solution.txt", "a", encoding="utf-8") as solution:
            solution.write(data_to_print+"\n")
    print(data_to_print)
