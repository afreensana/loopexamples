

no = int(input("enter a number:"))

if no < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(no > 0):
       sum += no
       no -= 1
   print("The sum is",sum)