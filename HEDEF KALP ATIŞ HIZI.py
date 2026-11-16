yaş=int(input("Yaşınızı giriniz: "))
max_kalp_atış_hızı=(220-yaş)
hedef_kalp_atış_hızı_aralığı=(max_kalp_atış_hızı*0.5,"-",max_kalp_atış_hızı*0.85)
print(hedef_kalp_atış_hızı_aralığı)