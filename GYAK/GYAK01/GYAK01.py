def contains_odd(input_list:list)->bool:
    for x in input_list:
        if (x%2)==1:
            return True
    return False

def is_odd(input_list:list) ->bool:
    bool_list=[]
    for x in input_list:
        if (x%2)==1:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return bool_list

