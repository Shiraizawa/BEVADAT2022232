def subset(input_list: list, start_index:int, end_index:int) -> list:
    return input_list[start_index:end_index]

def every_nth(input_list:list,step_size:int) -> list:
    new_list=[]
    for x in range(0,len(input_list),step_size):
        new_list.append(input_list[x])
    return new_list

def unique(input_list:list) ->bool:
    for x in range(0,len(input_list)-1,1):
        for y in range(x+1,len(input_list),1):
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
            is_unique=True
            for z in new_list:
                if y==z:
                    is_unique=False
            if is_unique:
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

def transpose(input_list:list)->list:
    new_list=[]
    for x in input_list:
        for y in x:
            if(new_list[x.index(y)]) is None:
                new_list[x.index(y)]=[]
            new_list[x.index(y)].append(y)
    return new_list

def split_into_chunks(input_list:list,chunk_size:int)->list:
    result_list=[]
    chunk_holder=[]
    for x in input_list:
        if(len(chunk_holder)>=chunk_size):
            result_list.append(chunk_holder)
            chunk_holder=[]
        chunk_holder.append(x)
    if chunk_holder is not None:
        result_list.append(chunk_holder)
    return result_list

def merge_dicts(*dict: dict)->dict:
    result_dict={}
    for x in dict:
        result_dict=result_dict | x
    return result_dict

def by_parity(input_list:list)->dict:
    result_dict={'even': [],'odd': []}
    for x in input_list:
        if(x%2)==0:
            result_dict['even'].append(x)
        else:
            result_dict['odd'].append(x)
    return result_dict

def mean_key_value(input_dict:dict)->dict:
    new_dict={}
    for key, value in input_dict.items:
        count=0
        sum=0
        for x in value:
            count=count+1
            sum=sum+x
        if count is not 0:
            new_dict.update(key,(sum/count))
    return new_dict