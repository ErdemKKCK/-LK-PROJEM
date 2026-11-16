kitaplar = ["Roman", "Tarih", "Bilgi", "Siir", "Atlas", "Masal"]
fiyatlar = [int(x) for x in input().split()]
bütçe=int(input())
def indirimli_sayılar():
    indirimli=[x*(9/10) for x in fiyatlar]
    return indirimli
    print(indirimli)
def ortalama_altı():
    a=sum(fiyatlar)/len(fiyatlar)
    c=[]
    for i in fiyatlar:
        if i<a:        
            c.append(i)
    return(c)
    print(c)
def butceyi_asan_sayisi(fiyatlar, bütçe):
    b=0
    for i in fiyatlar:
        if i>bütçe:
            b=b+1
    return b
    print(b)
def en_pahali_urun(fiyatlar, kitaplar):
    x=fiyatlar.index(max(fiyatlar))
    z=kitaplar[x]
    return z
    print(z)
print("İndirimli :",indirimli_sayılar())
print("Ortalama alti :",ortalama_altı())
print("Butceyi asan urun sayisi :",butceyi_asan_sayisi(fiyatlar, bütçe))
print("En pahali urun :",en_pahali_urun(fiyatlar, kitaplar))
