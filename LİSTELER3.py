#soldaki toplam ile sağdaki toplamın eşit olduğu indexi bulma
a=[1,2,3,4,5,5]
for i in range(len(a)):
    if sum(a[ :i])==sum(a[i:]):
        print("Eşitlik sağlanıyor")
        print(a.index(i))

#kullanıcıdan alınan listenin elemanlarının tiplerini kontrol etme
def type_check(lst):
    x=type(lst[0])
    for i in lst:
        if type(i)!=x:
            return False
    return True 
print(type_check([1,2,3,4,5]))

#kullanıcıdan alınan iki string veya iki intengerın toplamını hesaplayan fonksiyon
def sum_strange(a,b):
    if type(a) and type(b) == str:
        print(int(a)+int(b))
    elif type(a) and type(b) == int:
        print(str(a)+str(b))
print(sum_strange("1","2"))

#alınan iki integer arasında bulunan sayıları listeleyen fonksiyon
def genarete_list(a,b):
    a=[]
    for i in range(b):
        a.append(i)
    return a
print(genarete_list(0,5))

#ÖDEV
def merge_lst(lst1,lst2,lst3):
    a1=[]
    a2=[]
    a3=[]
    a4=[]
    for i in range (max(len(lst1),len(lst2),len(lst3))):
        if max(len(lst1),len(lst2),len(lst3)) > len(lst1):
            lst1.append("x")
        if max(len(lst1),len(lst2),len(lst3)) > len(lst2):
            lst2.append("Y")
        if max(len(lst1),len(lst2),len(lst3)) > len(lst3):
            lst3.append("Z")
    a1=a1+[lst1[0],lst2[0],lst3[0]]
    a2=a2+[lst1[1],lst2[1],lst3[1]]
    a3=a3+[lst1[2],lst2[2],lst3[2]]
    a4=a4+[lst1[3],lst2[3],lst3[3]]
    return a1,a2,a3,a4
print(merge_lst([1,2,3],[4,5],[6,7,8,9]))


z=[2,3]
y=[1,2,3,4,5]
print(max(len(z), len(y)))
