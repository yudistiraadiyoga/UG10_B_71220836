print('Selamat Datang di Program Pengurutan Bilangan')
print('Tentukan Pilihan Anda!!! [1/2]')

print('1. Ascending')
print('2. Descending')
print('')
pa1 = int(input('Masukkan Pilihan yang Anda Inginkan:'))
bp1 = input('Masukkan bilangan pertama :')
bp2 = input('Masukkan bilangan kedua :')
bp3 = input('Masukkan bilangan ketiga :')
bp4 = input('Masukkan bilangan keempat :')
l1 = [bp1,bp2,bp3,bp4]
if pa1 == 1:
     print('Urutan angka anda', sorted(l1))
elif pa1 == 2:
    print('Urutan angka anda', sorted(l1,reverse=True))
else:
    print('error')