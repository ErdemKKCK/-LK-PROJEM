import random
for roll in range(10):
    print(random.randrange(1,7))

import random
y1=0
y2=0
y3=0
y4=0
y5=0
y6=0
for roll in range(600):
    face=random.randrange(1,7)
    if face==1:
        y1=y1+1
    elif face==2:
        y2=y2+1
    elif face==3:
        y3=y3+1
    elif face==4:
        y4=y4+1
    elif face==5:
        y5=y5+1
    elif face==6:
        y6=y6+1
print(y1,y2,y3,y4,y5,y6,end=" ")