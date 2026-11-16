def karsılasma(isim):
    print(f"Merhaba {isim}")
karsılasma("Erdem")
karsılasma("MJ")

def topla(sayi1,sayi2):
    sonuc=sayi1+sayi2
    return sonuc
toplam_sonuc=topla(51,25)
print("sonuç :",toplam_sonuc)

def kuvvet_al(taban,us):
    return taban**us
sonuc=kuvvet_al(2,3)
print(sonuc)
print(kuvvet_al(5,3))

def hesapla(a, b):
    c= a + b, a * b
    return c
c=hesapla(4, 5)
print(c)

def karesi(sayi):
    s=sayi**2
    return s
print(karesi(15))

def maximum(d1,d2,d3):
    max_s=d1
    if d2>max_s:
        max_s=d2
    if d3>max_s:
        max_s=d3
    return max_s
print(maximum(1,2,3))



