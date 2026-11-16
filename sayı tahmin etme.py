import random
tahmin=int(input("1 ile 10 arasında bir sayı giriniz"))
sayı=random.randint(1,10)
devam=1
tahmin_sayısı=0
while devam==1:
    tahmin_sayısı=tahmin_sayısı+1
    if tahmin<sayı:
        tahmin=int(input("küçük sayı girdiniz tekrar deneyin"))
    if tahmin>sayı:
        tahmin=int(input("büyük sayı girdiniz tekrar deneyin"))
    if tahmin==sayı:
        break
print("doğru tahmin")
print(tahmin_sayısı+1)
    