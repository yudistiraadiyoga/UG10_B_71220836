print('PROGRAM PENGHITUNG VOLUME BANGUN RUANG')

print('Pilihan salah satu bangun ruang yang ingin dihitung volumenya:')
print('1.Limas')
print('2.Bola')
print('3.Prisma')
print('4.Kerucut')

p1 = input('Masukkan pilihan Anda:')
if 1:
    psal = input('Masukkan panjang sisi alas limas:')
    tl = input('Masukkan tinggi limas:')
    vl = 1/3*psal*tl
    print('Volume limas tersebut adalah',vl)
elif 2:
    pjjb = input('Masukkan panjang jari-jari bola:')
    phi = float('3,14')
    vb = 4/3*phi*pjjb**3
    print('Volume bola tersebut adalah',vb)
elif 3:
    print('pilihlah salah satu dari pilihan di bawah:')
    print('1.Prisma Segitiga')
    print('2.Prisma Segiempat')
    print('3.Prisma Segilima')
    p2 = input('tentukan pilihan Anda:')
    if 1:
        pjsp1 = input('Masukkan panjang sisi alas prisma:')
        tap1 = input('Masukkan tinggi alas prisma:')
        tps1 = input('Masukkan tinggi prisma segitiga')
        las1 = 1/2*tap1*pjsp1
        vps1 = las1*tps1
        print('Volume prisma segitiga tersebut adalah',vps1)
    elif 2:
        pjsp2 = input('Masukkan panjang sisi alas prisma:')
        tap2 = input('Masukkan tinggi alas prisma:')
        tps2 = input('Masukkan tinggi prisma segiempat')
        las2 = 6*pjsp2**2
        vps2 = las2*tps2
        print('Volume prisma segiempat tersebut adalah',vps2)
    elif 3:
        pjsp3 = input('Masukkan panjang sisi alas prisma:')
        tap3 = input('Masukkan tinggi alas prisma:')
        tps3 = input('Masukkan tinggi prisma segilima:')
        vps3 = (5/2*pjsp3*tap3)*tps3
        print('Volume prisma segilima tersebut adalah',vps3)
    else:
        print('Prisma yang anda cari belum tersedia di Kalkulator ini')
elif 4:
    jjk = input('Masukkan jari-jari kerucut:')
    tk = input('Masukkan tinggi kerucut:')
    phi = float('3,14')
    vk = 1/3*phi*jjk**2
    print('Volume prisma segilima tersebut adalah',vk)