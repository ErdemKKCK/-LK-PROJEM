gs=7
for hak in range(3,-1,-1):
    tahmın=int(input("gizli sayıyı tahmin et 3 hakkınız var"))
    if tahmın==gs:
            print("tebrikler bildiniz")
    elif hak==2:
        int(input("2 hakkınız kaldı"))
    elif hak==1:
        int(input("1 hakkınız kaldı"))
    elif hak==0:
        int(input("hakkınız bitti"))
    elif tahmın==gs:
        print("tebrikler bildiniz")
        