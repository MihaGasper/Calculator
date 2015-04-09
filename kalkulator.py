print "kalkulator"

print("vnesi stevilo x")
x = raw_input()
x=float(x)

print("vnesi stevilo y")
y = raw_input()
y=float(y)

print"vnesi operacijo"
operacije = raw_input()

if operacije == "sestevanje" or operacije == "+":
    ans = x+y
    print(ans)

elif operacije == "odstevanje" or operacije == "-":
    ans = x-y
    print(ans)

elif operacije == "mnozenje" or operacije == "*":
    ans = x*y
    print(ans)

elif operacije == "deljenje" or operacije == "/":
    ans = x/y
    ans = round(ans,2)
    print ans

else:
    print "not"

