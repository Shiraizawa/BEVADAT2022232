import numpy as np

#Készíts egy függvényt ami létre hoz egy nullákkal teli numpy array-t.
#Paraméterei: mérete (tupel-ként), default mérete pedig legyen egy (2,2)
#Be: (2,2)
#Ki: [[0,0],[0,0]]
#create_array()

def create_array(size: tuple = (2,2)):
     arr=np.zeros(size)
     return arr

#Készíts egy függvényt ami a paraméterként kapott array-t főátlót feltölti egyesekkel
#Be: [[1,2],[3,4]]
#Ki: [[1,2],[3,1]]
#set_one()

def set_one(array):
     np.fill_diagonal(array,1)
     return array

# Transzponáld a paraméterül kapott mártix-ot:
# Be: [[1, 2], [3, 4]]
# Ki: [[1, 2], [3, 4]]
# do_transpose()

def do_transpose(matrix):
     matrix=np.transpose(matrix)
     return matrix

# Készíts egy olyan függvényt ami az array-ben lévő értékeket N tizenedjegyik kerekíti, alapértelmezetten 
# Be: [0.1223, 0.1675], n = 2
# Ki: [0.12, 0.17]
# round_array()

def round_array(array, n:int=2):
     array=np.round(array,n)
     return array

# Készíts egy olyan függvényt, ami a bementként  0 és 1 ből álló tömben a 0 - False-ra az 1 True-ra cserélni
# Be: [[1, 0, 0], [1, 1, 1],[0, 0, 0]]
# Ki: [[ True False False], [ True  True  True], [False False False]]
# bool_array()

def bool_array(array):
     array=np.array(array, dtype=bool)
     return array

# Készíts egy olyan függvényt, ami a bementként  0 és 1 ből álló tömben a 1 - False-ra az 0 True-ra cserélni
# Be: [[1, 0, 0], [1, 1, 1],[0, 0, 0]]
# Ki: [[ True False False], [ True  True  True], [False False False]]
# invert_bool_array()

def invert_bool_array(array):
     array=np.array(array, dtype=bool)
     array=np.invert(array)
     return array

# Készíts egy olyan függvényt ami a paraméterként kapott array-t kilapítja
# Be: [[1,2], [3,4]]
# Ki: [1,2,3,4]
# flatten()

def flatten(array):
     array=array.flatten()
     return array
