#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if(my_list is not None):
        cp_list = my_list.copy()
        if idx < 0 or idx >= len(my_list):
            return my_list
        else:
            cp_list[idx] = element
            return cp_list
