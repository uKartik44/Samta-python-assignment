# Input values for the series  
num = int(input('Enter any number :'))
a, b = 0, 1
# Input number should not be 0 or less then zero 
if num <=0 :
    print('Please enter number greater than 0')
else:
    for i in range(0 , num):
        print( a, end=" ")
        c = a+b
        a = b
        b = c
