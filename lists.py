def remove_elements(list_to_remove_elements):
    largo= len(list_to_remove_elements)
    if largo < 5:
        return list_to_remove_elements[1:]
    #['Audi', 'BMW', 'Porsche', 'Aston Martin']

    elif largo == 5:
        return list_to_remove_elements[1:4]
    #['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    #  0       1         2        3       4         5
    elif largo >= 6:
        return list_to_remove_elements[1:4]+list_to_remove_elements[6:]

def add_elements(list_to_add_elements):
    list_to_add_elements= ["Pink"]+list_to_add_elements+["Yellow"]
    return list_to_add_elements


def is_empty(list_to_check):
    return list_to_check==[]

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1)<=2 or len(list_to_compare2)<=2:
        return False
    elif list_to_compare1[2]==list_to_compare2[2]:
        return True

#list_of_lists_to_modify = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
                            #0  1  2    0 1   2  3  4    0  1    2   3

def list_of_lists(list_of_lists_to_modify):
    a=list_of_lists_to_modify[0][:2]
    b= list_of_lists_to_modify[1][1:4]
    c=list_of_lists_to_modify[2][-2:]
    return [a,b,c]
