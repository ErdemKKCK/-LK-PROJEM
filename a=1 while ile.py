a=1
gs=7
hak=3
while a==1 and hak>0:
    gızlı_sayı=int(input(str(hak) + "deneme hakkınız var gizli sayıyı tahmin ediniz"))
    if gızlı_sayı==gs:
        print("doğru tahmin")
        a=0
    elif a==1 and hak>0:
        hak=hak-1
if hak==0:
 print("hakkınız bitti")
 