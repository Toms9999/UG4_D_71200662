print('='*20, 'BARIS ARITMATIKA', '='*20)

def aritmatika(a, s, d):
    total = (s/2) * (2*a + (s-1)*d)
    return total

a = int(input('Masukkan Bilangan awal : '))
d = int(input('Masukkan selisih bilangan : '))
s = int(input('Masukkan banyaknya suku : '))

hasil = aritmatika(a, s, d)
print('Total dari deret aritmatika tersebut adalah : ',hasil)