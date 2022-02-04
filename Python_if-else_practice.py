#1 A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.Ask user for their salary and year of service and print the net bonus amount.

salary = int(input("Enter salary"))
service_years = int(input("Enter service year"))
if service_years>5:
    print("Net Bonus amount is:",0.05*salary)
else:
    print("No Bonus")

#2 Take values of length and breadth of a rectangle from user and check if it is square or not.
l = int(input("Enter length"))
b = int(input("Enter breadth"))
if l==b:
    print("It is a square")
else:
    print("Not a square its a rectangle")

#3 Take two int values from user and print greatest among them.
x = int(input("Enter first number"))
y = int(input("Enter second number"))
if x>y:
    print(f"{x} is greater than {y}")
elif y>x:
    print(f"{y} is greater than {x}")
else:
    print("x and y are equal")

#4 A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity.Suppose, one unit will cost 100. Judge and print total cost for user.
quantity=int(input("Enter quantity"))
price=quantity*100
if price>=1000:
    disc=price*0.10
else:
    disc=0
print("Total cost is",price-disc)

#5 A school has following rules for grading system:
#a. Below 25 - F
#b. 25 to 45 - E
#c. 45 to 50 - D
#d. 50 to 60 - C
#e. 60 to 80 - B
#f. Above 80 - A
#Ask user to enter marks and print the corresponding grade.
marks = int(input("Enter the marks"))
if marks<25:
    print ("grade F")
elif marks>=25 and marks<45:
    print ("grade E")
elif marks>=45 and marks<50:
    print ("grade D")
elif marks>=50 and marks<60:
    print ("grade C")
elif marks>=60 and marks<80:
    print ("grade B")
else:
    print ("grade A") 
print(marks) 

#6 Take input of age of 3 people by user and determine oldest and youngest among them.
a = int(input("Enter age of a"))
b = int(input("Enter age of b"))
c = int(input("Enter age of c"))
if  a>b and a>c:
    print("a is oldest")
elif b>a and b>c:
    print("b is oldest")
else: 
    print("c is oldest")

#7 Write a program to print absolute value of a number entered by user. E.g.-INPUT: 1 -> OUTPUT: 1  INPUT: -1  -> OUTPUT: 1
num = int(input("Enter the number"))
if num<0:
  num=num*-1
print("absolute number is",num)

#8 A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.
held = int(input("No of classes held")) 
attended = int(input("No of classes attended"))
attendence = (attended/held)*100
if attendence >= 75:
    print("Student is allowed to sit in exam")
else:
    print("Student is not allowed to sit in exam") 
print(attendence)

#9 Write a program to calculate the electricity bill(accept nuber of unit from user) according to the following criteria:
#Unit Price first 100 units         no charge
#Next 100 units                      Rs 5 per unit              100-200
#After 200 units                     Rs 10 per unit             201-400
#Above that                          Rs 15 per unit              450
a = int(input("Enter Units"))
if a <= 100:
    print(a)
if a > 100 and a <= 200:
    b = a*5
    print(b)
if a > 200 and a <= 400:
    b = a*10
    print(b)
if a > 400:
    b=a*15
    print(b)
#10 Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria:
#Cost price(in Rs)                  Tax
#100000                              15%
#>50000 and <= 100000                10%
#<= 50000                             5%
price = int(input("Enter bike price"))
if price>100000:
    tax = price*0.15
elif price>=50000 and price<100000:
    tax = price*0.10
else:
    tax=price*0.05
print(tax)
print("you have to pay:",price+tax)

#11 Write a python program to check triangle is equilateral,isosceles or scalene
a = int(input("Enter first side"))
b = int(input("Enter second side"))
c = int(input("Enter third side"))
if (a==b and a==c):
    print("It's an Equilateral Triangle")
elif (a==b or b==c or c==a):
    print("It's a Isosceles Triangle")
else:
    print("It's a Scalene Triangle")

#12 Write a python program to find the median of three values
#Expected output: 
#Input first number : 15
#Input second number : 26
#Input third number : 29
#The median is 26.0
a = int(input("Enter value of a"))
b = int(input("Enter value of b"))
c = int(input("Enter value of c"))
l = [a,b,c]
print(l)
l.remove(min(l))
l.remove(max(l))
print(l[0])

#13 Write a python program to get next day of a given date.
#Expected output: Input a year : 2016  Input a month[1-12] : 08 Input a day[1-31] : 23
#The next date is [yyyy-mm-dd] 2016-8-24
year=int(input("Enter year"))  
month=int(input("Enter month")) 
date=int(input("Enter date"))    


if(year%4==0):
    leap_year=True
else:
    leap_year=False

if month in (1,3,5,7,8,10,12): #month
    month_len=31
elif(month==2):     #leap
    if (year%4):
        month_len=29
    else:
        month_len=28
else:
    month_len=30

if date<month_len:
    date += 1
else:
    date = 1


if month==12:
    month=1
    year+=1
else:
    if month<12 and date==1:
        month+=1
    

print(year ,month ,date)