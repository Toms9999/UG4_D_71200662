def cari_kata(kalimat):
    kata = kalimat.split
    kataterpanjang = [0]

for k in kalimat:
    if len(k) > len(kataterpanjang):
        kataterpanjang = k
        return kataterpanjang

kalimat = input('Masukkan sebuah Kalimat : ')


print('kata terpanjang dalam kalimat tersebut adalah : ', kataterpanjang)    

    
    