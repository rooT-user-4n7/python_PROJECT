# selection with if elif and else:

# N_number = 43

N_number = int(input("enter your number:"))
if(N_number>30):
    print("Number is Higher than 30")
elif(N_number>=10):
    print("number is greaterthan 10")
else:
    print("Number is lessthan 10")



year = int(input("enter your years:"))
if(year>=18):
    print("your are over 18 years!")
else:
    print("you are less then under 18!")



marks = int(input("enter your final or total mask:"))
if(marks>=80):
    print("A+")
elif(marks>=80):
    print("A")
elif(marks>=70):
    print("B+")
elif(marks>=60):
    print("B")
elif(marks>=50):
    print("C+")
elif(marks>=40):
    print("C")
else:
    print("Sorry You are GG>kick>you are fuck")

x = [10,20,50,"Aditya",2.5,"Trivedi",60]   
y = [30,10,60,"Aditya",2.5,"hello",60]  
print(x==y)



print("\n")
x = [10,20,50,"Aditya",2.5,"Trivedi",60]   
y = [10,20,50,"Aditya",2.5,"Trivedi",60]  
print(x==y)