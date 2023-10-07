#**********start if**********
# shart this m36-40(in the 36)
number1 = int(input("enter number 1:"))
number2 = int(input("enter number 2:"))
number3 = int(input("enter number 3:"))
if number1>number2 and number2>=number3 :
    print(number1)
elif number2>number1 and number1>=number3 :
        print(number2)
elif number3>number2 and number2>=number1 :
        print(number3)
# shart this m36-40(in the 37)
number1 = int(input("enter number 1:"))
number2 = int(input("enter number 2:"))
number3 = int(input("enter number 3:"))
if number1>number2 and number2>number3 :
    print(number1,number2,number3)
elif number1>number3 and number3>number2 :
    print(number1,number3,number2)
elif number2>number1 and number1>number3 :
    print(number2,number1,number3)
elif number2>number3 and number3>number1 :
    print(number2,number3,number1)
elif number3>number1 and number1>number2 :
    print(number3,number1,number2)
elif number3>number2 and number2>number1 :
    print(number3,number2,number1)
# shart this m36-40(in the 38)
number = int(input("enter number :"))
if number<=7 and number>=1 :
    print("week one")
elif number<=14 and number>=8 :
    print("week two")
elif number<=21 and number>=15 :
    print("week three")
elif number<=28 and number>=22 :
    print("week four")
elif number<=30 and number>=29 :
    print("week five")
# shart this m36-40(in the 39)
number=(input("enter number:"))
mmd=''
for i in number :
    if i=='1' :
        mmd+=i
print(mmd)
# shart this m36-40(in the 40)
def sum_binary():
    binary1 =(input("enter number 1:"))
    binary2 =(input("enter number 2:"))
    decimal1 = int(binary1, 2)
    decimal2 = int(binary2, 2)
    result = decimal1 + decimal2
    binary_result = bin(result)[2:]
    return binary_result
print(sum_binary())
#**********End if**********




#**********start for**********
# for this m66-70(in the 66)
def fibonacci(num):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return n in fib_sequence

count = 0
for _ in range(100):
    number = int(input("enter number :"))
    if number % 2 == 1 and fibonacci(number):
        count += 1
print(count)
# for this m66-70(in the 67)
def divisible(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return num % b == 0
num = int(input("enter number :"))
count = 0
for i in range(1, num + 1):
    if divisible(i):
        count += 1
print(f"{count}")
# for this m66-70(in the 68)
number =(input("enter number:"))
sum=0
for i in number :
    if i==("0") :
        sum +=1
print(sum)
# for this m66-70(in the 69)
number =(input("enter number:")).replace("0","")
print(number)
#and
number =(input("Enter number: "))
number_j=str("")
for i in number :
    if i != "0" :
     number_j += i
print(number_j)
# for this m66-70(in the 70)
for num in range(56, 1985):
    f = []
    for i in range(1, num + 1):
        if num % i == 0:
            f.append(i)
    print(f"{num}: {f}")
#**********End for**********



#**********start array**********
# array this m86-90(in the 86)
numbers=[]
number=int(input("enter number elemnt:"))

for i in range(number) :
    numberasli=int(input("enter number:"))
    numbers.append(numberasli)
max_number=max(numbers)
print(max_number)
# array this m86-90(in the 87)
arr_num=[]
number=int(input("enter element:"))
for i in range(number) :
    voroodi=int(input("enter number:"))
    arr_num.append(voroodi)
sort_num=sorted(arr_num,reverse=True)
print(sort_num)
# array this m86-90(in the 88)
number=(input("enter number/space:"))
arr_num=number.split()
sprted_number=sorted(arr_num)
if arr_num==sprted_number :
    print("yes")
else :
    print("no")
# array this m86-90(in the 89)
def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = []
for i in range(4):
    num = int(input(f"number {i+1}: "))
    numbers.append(num)

non_primes = []
for num in numbers:
    if not prime(num):
        non_primes.append(num)

print("gheyr aval")
print(non_primes)
# array this m86-90(in the 90)
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

numbers = []
while True:
    num = input("enter number: ")
    if num == "":
        break
    num = int(num)
    numbers.append(num)

for num in numbers:
    fact = factorial(num)
    print(f"{num}! = {fact}")
#**********End array**********
#**********End for**********



#**********start function**********
# function this m106-110(in the 106)
def zoj():
 arr_num=[]
 for i in range(5):
     num=int(input("enter number:"))
     arr_num.append(num)
 for num in arr_num :
         if num%2==0:
             print(num)
zoj()
# function this m106-110(in the 107)
def find_different_numbers(numbers):
    average = sum(numbers[:3]) / 3
    different_numbers = [num for num in numbers if num != average]
    return different_numbers
numbers = []
for i in range(5):
    number = int(input("Enter number {}: ".format(i+1)))
    numbers.append(number)
different_numbers = find_different_numbers(numbers)
print(different_numbers)
# function this m106-110(in the 108)
def prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
n = int(input("enter number elemnt: "))
numbers = []
for i in range(n):
    number = int(input("enter number: "))
    numbers.append(number)
count = 0
for number in numbers:
    if prime(number):
        count += 1
print("addad aval number:", count)
# function this m106-110(in the 109)
def fact() : 
 zarb=1
 num_el=int(input("enter number element:"))
 for i in range(num_el) :
     voroodi=int(input("enter number:"))
 for i in range(1,voroodi+1):
        zarb*=i
        print(zarb)    
    
fact()
# function this m106-110(in the 110)
def bozorg() : 
 arr_num=[]
 num_el=int(input("enter number element:"))
 for i in range(num_el) :
     voroodi=int(input("enter number:"))
     arr_num.append(voroodi)
 sorted_bozorg=sorted(arr_num,reverse=True)
 print(sorted_bozorg)
bozorg()
#**********End function**********



#**********start string**********
# string this m117-121(in the 117)
str_in=(input("enter string:"))
str_Bold=str_in.title()
print(str_Bold)
# string this m117-121(in the 118)
import re
str_in=(input("enter string:"))
numbers = re.findall('\d+', str_in)
print(numbers)
# string this m117-121(in the 119)
str_in=(input("enter string:"))
str_remove=str_in.replace("a","")
print(str_remove)
# string this m117-121(in the 120)
str_in=(input("enter string:"))
str_remove=str_in.replace(" ","")
print(str_remove)
# string this m117-121(in the 121)
nuber1=int(input("enter number1 16 raghami:"))
nuber2=int(input("enter number2 16 raghami:"))
str_sum=str(nuber1+nuber2)
print(str_sum)
#**********End string**********
#my name is sajadafsar