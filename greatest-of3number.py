def greatest():

    a=int(input("enter the number a:"))
    b=int(input("enter the number b:"))
    c=int(input("enter the number c:"))

    print("VALUE OF a:",a)
    print("VALUE OF b:",b)
    print("VALUE OF c:",c)


    if((a>b) and (a>c)):
        print("a is greatest")

    if((b>a) and (b>c)):
        print("b is greatest")

    if((c>a)and(c>b)):
        print("c is greatest")

greatest()
