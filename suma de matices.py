matrix_a  = [[1,2,3],
             [4,5,6],
             [7,8,9]]

matrix_b  = [[1,2,3],
             [4,1,2],
             [1,1,0]]

result_sum = [] #Contendra el resultado de la suma de las dos matrices

for row in range (len(matrix_a)): #esta linea itera las filas de la matrix A
    sum_list = []                   #Lista vacias para almacenar lo elementos
    for column in range (len (matrix_a[0])): #esta itera las columnas de matix A
        sum_list.append (matrix_a[row][column] + matrix_b[row][column]) #Esta línea de coigo agrega a la lista vacia, la suma de las matrices
    result_sum.append (sum_list) #se agregan a la lista que alverga el resultado

#esta linea de codigo preseta en pantalla la iteración y resultado. 
for row in range (len (matrix_a)):
    if row != 1:
        print ( f"{matrix_a[row]}   {matrix_b[row]}   {result_sum} ")
    else:
        print (f"{matrix_a[row]} + {matrix_b[row]} = {result_sum} ")

