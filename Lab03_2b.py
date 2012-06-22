num=raw_input("Enter Number: ")
number=int(num)
while number:
   
    digit = number % 10
    print number , 
# do whatever with digit
    number /= 10
