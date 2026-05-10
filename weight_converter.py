weight=int(input("enter your weight"))
unit =input("(L)bs or (K)g: ") 
if unit.upper()=="L":
    convertor=weight*0.45
    print(f"Your weight is : {convertor} in kilo")  
else:
    convertor=weight/0.45
    print(f"Your weight is {convertor} in pound")
