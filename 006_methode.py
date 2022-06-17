
# memanggil sebuah fungsi berdasarkan dari objek
# beberapa methode tidak bisa didefinisikan & di print

keluarga = ['irin', 4.23, 'agus', 4.69, 'sena', 4.36, 'dian', 4.81]
adik = 'dian'

print('\n versi 1 : ', keluarga)
print( '\n versi 2 : ', keluarga.index('sena'))
print( '\n versi 3 : ', keluarga.count(4.23))
print( '\n versi 4 : ', keluarga.count(2))
print( '\n versi 5 : ', len(keluarga))
print( '\n versi 6 : ', adik.capitalize())
print( '\n versi 7 : ', adik.replace('d', 'andr'))

# methode yang tidak bisa dengan print & didefinisikan
keluarga_tambahan = keluarga[:]
keluarga_tambahan.append('abi')
keluarga_tambahan.append(4.69)
keluarga_none = keluarga_tambahan.append(69999999)
print( '\n versi 8 : ', keluarga_tambahan)
print( '\n versi none1 : ', keluarga_tambahan.append(69))
print( '\n versi none2 : ', keluarga_none)