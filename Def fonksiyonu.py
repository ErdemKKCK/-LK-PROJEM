def bilgi_ver ():
    print("sa")
bilgi_ver()

def karesini_al(sayi):
    sonuc=sayi**2
    return sonuc
print(karesini_al(5))

def topla(a,b):
    return a+b
print(topla(3,5))

def ortalama_hesaplama(liste):
        toplam = sum(liste)
        adet=len(liste)
        ortalama=toplam/adet
        print(f"Ortalama: {ortalama}")
ortalama_hesaplama([1,2,3,4,5])
