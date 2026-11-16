dogru=123
hak=3
a=True
while hak>0 and a==True:
    sifre=int(input(str(hak) + "deneme hakkınız var şifrenizi giriniz")) 
    if sifre==dogru:
        print("doğru şifre")
        a=False
    elif a==True and hak>0:
        hak=hak-1
if hak==0:
    print("hakkınız bitti")
    