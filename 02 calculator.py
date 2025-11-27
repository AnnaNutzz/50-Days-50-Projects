a = int(input("enter a: "))
b = int(input("enter b: "))

opt = input("action? :")
if opt=="+":
    print(a+b)
elif opt=="-":
    print(a-b)
elif opt=="*":
    print(a*b)
elif opt=="%":
    print(a%b)
else:
    print("not a valid operation")
