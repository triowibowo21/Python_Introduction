import numpy as np

tinggi = [1.73, 1.68, 1.71, 1.89, 1.79]
lebar = [65.4, 59.2, 63.8, 88.4, 68.71]

np_tinggi = np.array(tinggi)
np_lebar = np.array(lebar)

print('np_tinggi :', np_tinggi)
print('np_lebar :', np_lebar)



# operari bagi dan pangkat 
# hasil = lebar / tinggi **2
# print('\n hasil :', hasil) # tidak bisa dilakukan operasi

hasil = np_lebar / np_tinggi **2
print('\n hasil :', hasil)
print('\n hasil[1] :', hasil[1])
print('\n hasil > 23 :', hasil > 23)
print('\n hasil > 23 :', hasil[hasil > 23])



# perbedaan list & array
python_list = [1,2,3]
numpy_array = np.array([1,2,3])

python_list = python_list + python_list
print('\n python_list :', python_list)
print('\n python_list[1] :', python_list[1])


print('\n numpy_array :', numpy_array)
numpy_array = numpy_array + numpy_array
print('\n numpy_array :', numpy_array)
print('\n numpy_array[0] :', numpy_array[0])
print('\n numpy_array > 5 :', numpy_array > 5)
print('\n numpy_array > 5 :', numpy_array[numpy_array > 5])



#operasi perkalian
# python_list = python_list * python_list
# print('\n python_list :', python_list) # tidak bisa dilakukan perkalian

numpy_array = numpy_array * numpy_array
print('\n numpy_array :', numpy_array)


# operasi array dengan panjang berbeda
bilangna5 = np.array([1,2,3,4,5])
bilangan6 = np.array([1,2,3,4,5,6])

# jumlah = bilangna5 + bilangan6
# print('\n jumlah :', jumlah) # ValueError: operands could not be broadcast together with shapes (5,) (6,) 
# tidak bisa dilakukan

bilangna5 = np.append(bilangna5, [6])
print('\n bilangna5 :', bilangna5)
