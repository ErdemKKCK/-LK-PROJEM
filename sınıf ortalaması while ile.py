deger=int(input("Lütfen bir notunuzu giriniz bitirmek için-1 giriniz: "))
kisi=0
toplam=0
while deger>0:
    kisi=kisi+1
    toplam=toplam+deger
    deger=int(input("notunuzu girmeye devam ediniz bitirmek için -1 giriniz: "))
if deger==-1:
    print("Not girişi bitmiştir.")
ortalama=toplam/kisi
print("Sınıfın ortalaması: ", ortalama)
