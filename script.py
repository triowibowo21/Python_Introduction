import numpy as np

keluarga = ['irin', 4.23, 'agus', 4.69, 'sena', 4.36, 'dian', 4.81]
tam_kel = keluarga + ['abi', 4.69]

print(str(len(tam_kel)) + " elmen didalam list tamb_kel \n")
print("isi elmen didalam list tamb_kel : \n", tam_kel)
print("tipe list tamb_kel : ", type(tam_kel))

np_kel = np.array(tam_kel)

print("\n isi elmen didalam list np_kel : \n", np_kel)
print("tipe list np_kel : ", type(np_kel))
