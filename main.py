from Multipoly import Multipoly 
from Multi_Linear_Reg import Multi_Linear_Reg
import numpy as np

d_arr = [3, 4, 7, 6]
x_arr = [[1, 2, 3, 4]]

#x_arr.append(d_arr)

#print(x_arr)
y_arr = [2, 3, 5, 4]
r_arr = [11, 13, 17, 14]

# Stellen Sie sicher, dass y_arr und r_arr die gleiche Länge haben

#y_arr.append(r_arr)

print(y_arr)
reg = Multi_Linear_Reg(x_arr, y_arr)
reg.create_matrix()
reg.calculate_solv_solution()

#matrix = [[1 ,1, 1, 1],
 #[1, 2 ,3 ,4],
 #[3 ,4, 7, 6]]

#print(matrix)

#fin_matrix = np.matmul(matrix, np.transpose(y_arr))

#print(fin_matrix)




