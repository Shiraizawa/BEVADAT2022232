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

def element_wise_sum(input_list_1:list,input_list_2:list)->list:
    new_list=[]
    for x in range(0,len(input_list_1),1):
        for y in range(0,len(input_list_2),1):
            new_list.append(input_list_1[x]+input_list_2[y])
    return new_list
    