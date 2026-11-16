def ort(*liste):
   a=sum(liste)/len(liste)
   return a
print(ort(1,2,3))

notlar=[25,36,1234,34,123,356,234,789]
print(ort(*notlar))
