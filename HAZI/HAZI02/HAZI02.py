import numpy as np

# Írj egy olyan fügvényt, ami megfordítja egy 2d array oszlopait
# Be: [[1,2],[3,4]]
# Ki: [[2,1],[4,3]]
# column_swap()

def column_swap(array):
    array=np.flip(array, 1)
    return array

#Készíts egy olyan függvényt ami összehasonlít két array-t és adjon vissza egy array-ben, hogy hol egyenlőek 
# Pl Be: [7,8,9], [9,8,7] 
# Ki: [1]
# compare_two_array()
# egyenlő elemszámúakra kell csak hogy működjön

def compare_two_array(array1, array2):
    result=np.where(array1[::] == array2[::])
    return result


#Készíts egy olyan függvényt, ami vissza adja a megadott array dimenzióit:
# Be: [[1,2,3], [4,5,6]]
# Ki: "sor: 2, oszlop: 3, melyseg: 1"
# get_array_shape()
# 3D-vel még műküdnie kell!

def get_array_shape(array):
    result_array=np.array(np.shape(array))
    print(result_array)
    if len(result_array)<3:
        melyseg=1
    else:
        melyseg=result_array[2]
    return "sor: {}, oszlop: {}, melyseg: {}".format(result_array[0], result_array[1], melyseg)
