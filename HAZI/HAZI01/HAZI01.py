def subset(input_list: list, start_index, end_index) -> list:
    return input_list[start_index:end_index+1]

def every_nth(input_list:list,step_size) -> list:
    new_list=[]
    for x in range(0,len(input_list),step_size):
        new_list.append(input_list[x])
    return new_list

def unique(input_list:list) ->bool:
    for x in range(0,len(input_list)-1,1):
        for y in range(x,len(input_list),1):
            if(input_list[x]==input_list[y]):
             return False
    return True

def flatten(input_list:list) ->list:
    new_list=[]
    for list in input_list:
        for x in list:
            new_list.append(x)
    return new_list

def merge_lists(*args)->list:
    new_list=[]
    for x in args:
        for y in x:
            if y not in new_list:
                new_list.append(y)
    return new_list

def reverse_tuples(input_list:list)->list:
    reverse_list=[]
    for x in input_list:
        reverse_list.append(x.reverse())
    return reverse_list

def remove_duplicates(input_list:list)->list:
    new_list=[]
    for x in input_list:
        is_duplicate=False
        for y in new_list: 
            if input_list[x]==new_list[y]:
                is_duplicate=True
        if not is_duplicate:
            new_list.append(input_list[x])
    return new_list
