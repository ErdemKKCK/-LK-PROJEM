def işlem(a,b,c):
    if c=="+":
        print(a+b)
    elif c=="-":
        if a>b:
            print(a-b)
        elif a<b:
            print(b-a)
    elif c=="*":
        print(a*b)
işlem(10,5,"")
    
