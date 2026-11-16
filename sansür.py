mystr=input("METİN GİRİN:")
def name(mystr):
    position=0
    uzunluk=len(mystr)
    txt=""
    for i in mystr:
        if position<uzunluk-2:
            txt=txt+"*"
        else:
            txt=txt+i
        position=position+1
    return txt
print(name(mystr))

