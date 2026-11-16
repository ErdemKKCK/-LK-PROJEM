a=input("İSİM GİRİNİZ")
def isim(a):
    uzunluk=len(a)
    txt=""
    p=0
    for i in a:
        if p<uzunluk-2:
            txt=txt+"*"
        else:
            txt=txt+i
        p=p+1
    return txt
print(isim(a))
