def sfd():
    global a1,b1,b
    if a1 in c1:
        b = c1.replace(f"{a1}","")
        return b
    else:
        pass
a1 = input(int())
b1 = input(int())
c1 = input(int())
a = a1 + b1
b = sfd()
c = a1+b1+c1 
print(f"a = {a},b = {b},c = {c}")
