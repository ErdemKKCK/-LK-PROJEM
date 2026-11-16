c=[1, 2, 3]
print(c[3-5]) #TAM SAYI OLARAK KULLANILABİLİYOR
print(c[-2])

print(len(c))

c[2] = 17      #MUTUABLE OLDUĞU İÇİN DEĞİŞTİRİLEBİLİYOR
print(c)     

print(c[0]+c[1]+c[2]) #ELEMANLARI TOPLAYARAK YAZDIRMA

bos_liste=[]
for i in range(1,6):
    bos_liste=bos_liste+[i]
print(bos_liste) 

my_str=[]
my_str+="Merhaba"
my_str+="Elma"
print(my_str) #ELEMANLARI HARF HARF YAZDIRIR

LİST1=["Elma","Armut","Muz"]
LİST2=[1,2,3,4,5]
print(LİST1+LİST2) #LİSTELERİ TOPLAMAK İÇİN + İŞARETİ KULLANILABİLİR

sayilar = [5, 2, 2, 3, 4, 4, 1]
benzersiz_sayilar = set(sayilar)# set() fonksiyonu ile tekrar eden sayıları kaldırıp benzersiz sayıları elde edebiliriz
print(benzersiz_sayilar) 

x=["a","b","c"]
y=["a","c","d","e"]
boş=[]
for i in x+y:
    if i not in boş: # set() fonksiyonu kullanmadan tekrar eden sayıları kaldırıp benzersiz sayıları elde edebiliriz
        boş+=[i]
print(boş) 

yeni=[]
m=[1,2,3,4,5]
for i in range (len(m)-1):
    print(m[i]+m[i+1])
    if (m[i]+m[i+1])%2==1:
        print("Toplam tek")
        ü=("Toplam tek")
        yeni+=[ü]
    elif (m[i]+m[i+1])%2==0:
        print("Toplam çift")
        ğ=("Toplam çift")
        yeni+=[ğ]
print(yeni)