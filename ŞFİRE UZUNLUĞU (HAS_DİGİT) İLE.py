şifre=input("Lütfen şifrenizi giriniz: ")
uzunluk=len(şifre)
if uzunluk<6:
    print("very weak")
elif 6<=uzunluk<=9:
    if has_digit:
        print("medium")
    else:
        print("weak.")
else:
    if has_digit:
        print("very strong")
    else:
        print("strong")