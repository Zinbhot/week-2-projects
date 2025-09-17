#Print numbers from 1 to 10 using a for loop.
print("question1")
for x in range(1,11):
    print(x)
a=123445678900
print(a)#this can be used as a margin line between questions
#Print all numbers from 1 to 10 except 7, using continue.
print("question2")
for x in range(1,11):
    if x==7:
        continue
    print(x)
a=123445678900
print(a)
# Using a while loop, print numbers from 5 to 15.
print("question3")
x=5
while x<=15:
    print(x)
    x=x+1
a=123445678900
print(a)
#Print numbers 1–10, but stop when you reach 6 (use break).
print("question4")
for x in range(1,10):
    if x==6:
        break
    print(x)
a=123445678900
print(a)
#Print all even numbers from 1 to 20.
print("question5")
for x in range(1,21):
    if x%2!=0:
        continue
    print(x)
a=123445678900
print(a)
#Print numbers 1–20, but skip numbers divisible by 3.
print("question6")
for x in range(1,21):
    if x%3==0:
        continue
    print(x)
a=123445678900
print(a)
#Print numbers from 10 down to 1 using a for loop.
print("question7")
x=11
while x>=2:
    x=x-1
    print(x)
a=123445678900
print(a)
#Print numbers 1–15, but skip 5 and 9 (use continue).
print("question8")
for x in range(1,16):
    if x==5 or x==9:
        continue
    print(x)
a=123445678900
print(a)
#Using a while loop, print numbers starting from 1, double each time, stop when number ≥ 100.
print("question9")
x=1
while x<=100:
    print(x)
    x=x*2
a=123445678900
print(a)
#Using a while loop, print numbers from 1 to 50, stop if number is divisible by 13.
print("question10")
x=0
while x<12:
    x=x+1
    print(x)
print(a)
print("question11")
#Print numbers 1–100, but skip multiples of 4 and stop if number divisible by 25.
for x in range(1,100):
    if x%4==0:
        continue
    if x%25==0:
        break
    print(x)
#Using a for loop, print the first 10 odd numbers.
print("question12")
for x in range(1,20):
    if x%2==0:
        continue
    print(x)
#Print numbers from 1–50, but skip numbers divisible by 2 or 5.
print("question13")
x=1
while x<=50:
    x+=1
    if x%2==0 or x%5==0:
        continue
    print(x)
print("question13_answer2")
for x in range(1,50):
    if x%2==0 or x%5==0:
        continue
    print(x)
print("question14")
#Using a while loop, print numbers from 1–20, but replace multiples of 3 with “Fizz”.
x = 1
while x <= 20:
    if x % 3 == 0:
        print("Fizz")
    else:
        print(x)
    x += 1

print("question15")
#Write a loop that prints numbers from 1–50, but:
# Skip even numbers
# Stop completely if the number is divisible by 17
for x in range(1,50):
    if x%2==0:
        continue
    if x%17==0:
        break
    print(x)
