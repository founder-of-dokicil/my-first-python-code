# Sekuensial
print('ibu berkata "pergi ke toko"')
print('budi menjawab "baik, apa yang harus saya lakukan di toko?"')
print('ibu menjawab "beli 1 botol susu, jika ada telur beli 6"')
print('maka budi berangkat ke toko')
print('dan mulai berbelanja.')

# Percabangan
jumlah_botol_susu = 10
harga_susu = 10000
jumlah_susu_yang_dibeli = 9
jumlah_uang = 100000
if jumlah_botol_susu != 0 and jumlah_botol_susu > jumlah_susu_yang_dibeli:
    print(f'botol susu yang tersedia {jumlah_botol_susu} botol')
    print('budi mengecek harganya')
    print(f'harga satu botol susu adalah Rp. {harga_susu}')
    print(f'total harga {jumlah_susu_yang_dibeli} susu adalah Rp. {harga_susu * jumlah_susu_yang_dibeli}')
    print(f'budi membawa uang Rp. {jumlah_uang}')
    if jumlah_uang > harga_susu * jumlah_susu_yang_dibeli:
        print(f'budi membeli {jumlah_susu_yang_dibeli} botol susu')
else:
    print('budi membeli 1 botol susu')

