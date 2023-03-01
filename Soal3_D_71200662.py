def cari_kata(kalimat):
    kata = kalimat.split()

    kataterpanjang = kata[0]
    for k in kata:
        if len(k) > len(kataterpanjang):
            kataterpanjang = k
    return kataterpanjang

kalimat = input('Masukkan sebuah Kalimat : ')
kataterpanjang = cari_kata(kalimat) 

print('kata terpanjang dalam kalimat tersebut adalah : ', kataterpanjang)    
