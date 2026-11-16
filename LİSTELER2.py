a=[0,1,2,3,4,5,6]
print(a[0:8:2])

# insert kullanımı
liste3 = ["elma", "muz"]
liste3.insert(1, "armut")
print(liste3) 

#APPEND KULLANIMI
b=[1,2]
b.append([3,4])
print(b)

#EXTEND KULLANIMI
c=[1,2]
c.extend([3,4])
print(c)

#count
responses = [1, 2, 5, 4, 3, 5, 2, 1, 3,3,1, 4, 3, 3, 3, 2, 3, 3, 2,]
print(responses.count(3))

#reverse
m=[1,2,3]
m.reverse()
print(m)

#copy
n=[1,2,3]
o=n.copy()
print(o)

#pop
meyveler=["elma","armut","muz"]
s_meyve=meyveler.pop()
print(s_meyve)
print(meyveler)

#List Comprehensions
list1=[]
for i in range(1,6):
    list1.append(i)
print(list1)

#KISA YOL
list2=[a**2 for a in range(1,7) if a%2==0]
print(list2)

#SPLİT
a="YUSUF BİR EJDERHA"
b=a.split()
print(b)

