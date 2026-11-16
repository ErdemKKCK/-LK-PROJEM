yaş=int(input("Yaşınızı Giriniz:"))
seans_saati=float(input("Seans saatini seçiniz "))
durum=input("Öğrenci misiniz? (E/H):")
if yaş <6:
    print("Ücretsiz")
elif 6<= yaş <18 :
    if durum == "E":
        print("Öğrenci indirimiyle 80 TL")
    else:
        print("100 TL")
elif 18<=yaş<=64:
    if seans_saati >= 17.00:
        if durum == "E":
            print("Öğrenci indirimiyle 120 TL")
        else:
            print("150 TL")
    else:
            if durum == "E":
                print("Öğrenci indirimiyle 150 TL")
            else:
                print("200 TL")
else :
    print("70 TL")