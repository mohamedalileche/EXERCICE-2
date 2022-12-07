num_1 = int (input ("input the first number"))
num_2 = int (input ("input the second number"))
operator = int (input ("enter the operator \n 1=+ \n 2=- \n 3=* \n 4=/ "))


if operator == 1: 
    print ("the result of addition is ",num_1+num_2)
elif operator == 2:
    print ("the result of substraction is",num_1-num_2)
elif operator == 3:
    print ("the result of multiplication",num_1*num_2)   
elif operator == 4: 
    print ("the result of division",num_1/num_2)     
   
