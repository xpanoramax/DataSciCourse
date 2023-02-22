### Data Initialization

listObat = [
    ['Fish Oil', 30, 98000],
    ['Minyak Tawon', 20, 18000 ],
    ['Vitamin D', 80, 35000]
]

cart = []

while True:
    pilihanMenu = input('''
        Selamat Datang di Apotek Panorama
        
        List Menu:
        1. Menampilkan Daftar Obat
        2. Menambah Obat
        3. Menghapus Obat
        4. Membeli Obat
        5. Exit
        Masukkan angka Menu yang ingin dijalankan : ''')

### Read Data Function    
    if(pilihanMenu == '1'):
        print('Daftar Obat\n')
        print('Index\t Nama     \t| Stok\t| Harga')
        for i in range(len(listObat)):
            print('{}\t {} \t| {}\t| {}'.format(i,listObat[i][0],listObat[i][1],listObat[i][2]))

### Create Data Function   
    elif(pilihanMenu == '2'):
        namaObat = input('Masukkan  Nama Obat : ')
        stokObat = int(input('Masukkan Stok Obat : '))
        hargaObat = int(input('Masukkan Harga Obat : '))
        listObat.append([namaObat,stokObat,hargaObat])
        print('Daftar Obat\n')
        for i in range(len(listObat)):
            print('{}\t {}  \t| {}\t| {}'.format(i,listObat[i][0],listObat[i][1],listObat[i][2]))

### Delete Data Function       
    elif(pilihanMenu == '3'):
        print('Daftar Obat\n')
        print('Index\t|Nama     \t| Stok\t| Harga')
        for i in range(len(listObat)):
            print('{}\t {}  \t| {}\t| {}'.format(i,listObat[i][0],listObat[i][1],listObat[i][2]))
        indexObat = int(input('Masukkan index obat yang ingin dihapus: '))
        del listObat[indexObat]
        print('Daftar Obat\n')
        print('Index\t| Nama \t| Stock\t| Harga')
        for i in range(len(listObat)):
            print('{}\t {}  \t| {}\t| {}'.format(i,listObat[i][0],listObat[i][1],listObat[i][2]))

### Belanja           
    elif(pilihanMenu == '4'):
        print('Daftar Obat\n')
        print('Index\t|Nama \t Stok\t| Harga')
        for i in range(len(listObat)):
            print('{}\t| {} \t| {}\t| {}'.format(i,listObat[i][0],listObat[i][1],listObat[i][2]))
        while True:
            indexObat = int(input('Masukkan index obat yang ingin dibeli: '))
            qtyObat = int(input('Masukkan jumlah obat yang ingin dibeli: '))
            if(qtyObat>listObat[indexObat][1]) :
                print('Stok kurang, stok {} sisa {}'.format(listObat[indexObat][0],listObat[indexObat][1]))
            else:
                cart.append([listObat[indexObat][0], qtyObat, listObat[indexObat][2],indexObat])
            print('Isi Keranjang : ')
            print('Nama\t|      Qty\t| Harga')
            for item in cart:
                print('{}\t| {}\t| {}'.format(item[0],item[1],item[2]))
            checker = input('Ada tambahan belanja? (ya/tidak)=')
            if(checker == 'tidak'):
                break
        print('Daftar Belanja :')
        print('Nama\t| Qty\t| harga\t| Total Harga')
        totalHarga = 0
        for item in cart:
            print('{}\t {}\t| {}'.format(item[0],item[1],item[2]))
            totalHarga += item[1]*item[2]
        while True:
            print('Total yang Harus Dibayar = {}'.format(totalHarga))
            jmlUang = int(input('Masukkan Jumlah Uang: '))
            if(jmlUang>totalHarga):
                kembali = jmlUang - totalHarga
                print('Terima Kasih \n\nUang kembalian anda : {}'.format(kembali))
                for item in cart:
                    listObat[item[3]][1] -+ item[1]
                cart.clear()
                break
            elif(jmlUang==totalHarga):
                print('Terima Kasih')
                break
            else:
                kekurangan = totalHarga - jmlUang
                print('Uang Anda Kurang Sebesar {}'.format(kekurangan))
    
    elif(pilihanMenu ==5):
        break