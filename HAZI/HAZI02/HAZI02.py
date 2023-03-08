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

# Készíts egy olyan függvényt, aminek segítségével elő tudod állítani egy neurális hálózat tanításához szükséges Y-okat egy numpy array-ből. 
#Bementként add meg az array-t, illetve hogy mennyi class-od van. Kimenetként pedig adjon vissza egy 2d array-t, ahol a sorok az egyes elemek. Minden nullákkal teli legyen és csak ott álljon egyes, ahol a bementi tömb megjelöli
# Be: [1, 2, 0, 3], 4
# Ki: [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# encode_Y()

def encode_Y(array:np.array,length:int):
    new_array = []
    for x in array:
        holder_array=np.zeros(length,dtype=int)
        holder_array[x]=1
        new_array.append(holder_array)
    new_array=np.asarray(new_array)
    return new_array

# A fenti feladatnak valósítsd meg a kiértékelését. Adj meg a 2d array-t és adj vissza a decodolt változatát
# Be:  [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# Ki:  [1, 2, 0, 3]
# decode_Y()

def decode_Y(array:np.array):
    result_array=[]
    result_array.append(np.where(array==1)[1])
    return result_array

array = np.array([[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]])
print(decode_Y(array))