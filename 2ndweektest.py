a=12345678900
print(a)
#Using a while loop, print numbers from 1 to 50, stop if number is divisible by 13.
x=1
while x<=50:
    if x%13==0:
     break
     print(x)
    x+=1


#Print numbers 1–15, but skip 5 and 9 (use continue).
for x in range(1,16):
    if x==5 or x==9:
        continue
    print(x)
a=123445678900
print(a)
#Using a while loop, print numbers starting from 1, double each time, stop when number ≥ 100.
x=1
while x<=100:
    print(x)
    x=x*2
a=123445678900
print(a)