keluarga = ['irin', 4.23, 'agus', 4.69, 'sena', 4.36, 'dian', 4.81]
print('\n versi 1', keluarga)
keluarga[5] = 4.42
print('\n versi 2', keluarga)
keluarga[:2] = ['khairin', 4.12]
print('\n versi 3', keluarga)

# menambahkan elment baru
tambah_keluarga = keluarga + ['gery', 4.23]
print('\n versi 4', tambah_keluarga)

# menghapus sebuah elment
del(keluarga[2]) # menghapus nama agus
print('\n versi 4', keluarga)

del(keluarga[2]) # 4.69
print('\n versi 5', keluarga)

keluarga.remove('dian')
print('\n versi 6', keluarga)