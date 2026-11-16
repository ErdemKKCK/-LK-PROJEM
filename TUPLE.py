student_tuple=("Ali", "Veli", 3.3)
print(student_tuple)
print(len(student_tuple))

TUPLE1=(10,20,30)
TUPLE2=TUPLE1
TUPLE1+=(40,50)
print(TUPLE1)
print(TUPLE2)

#Enumarate
a=["apple","lemon"]
y=list(enumerate(a))
print(y)

#SEQUENCE SLİCİNY
a=[1,2,3,4,5]
print(a[2:4])

#DEL STATEMENT
numbers=list(range(1,11))
del numbers[-10]
print(numbers)

def modify_objects(items):
    for i in range(len(items)):
        items[i]=items[i]*2
    return items
a=[1,3,5]
print(modify_objects(a))

#SORT
a=[8,6,2,4]
a.sort()
print(a)

#SORTED
a=[3,1,2,4]
a1=sorted(a)
print(a1)
b=("ERDEM")
b1=sorted(b)
print(b1)

numbers=[1,2,3,4,5]
print(numbers.index(3))
print(numbers.index(3,2))