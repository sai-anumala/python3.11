print("****Welcome to our calculator!****")
while True:
    
    op=input("\nWhich type of calculator do you want to use? \n1.General\n2.Expression\n3.Exit\nEnter your choice: ")
   
    if op=='3':
        print("\n* * * * Thank you for using our calculator! * * * * ")
        break
    
    elif op=='1':
        print("\nChoose an operation:")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        op=int(input("\nEnter your choice: "))
        num1=float(input("\nEnter the first number: "))
        num2=float(input("\nEnter the second number: "))
        
        if op==1:
            print(f"\nAddition of {round(num1)} and {round(num2)} is {round(num1+num2)}")
            if input("\nIf you want value in decimal press Y else N: ")=='y'or'Y':
                print(f"\nAddition of {num1} and {num2} is {num1+num2}")
       
        elif op==2:
            print(f"Subtraction of {round(num1)} and {round(num2)} is {round(num1-num2)}")  
            if input("If you want value in decimal press Y else N: ")=='y'or'Y':
                print(f"Subtraction of {num1} and {num2} is {num1-num2}")
       
        elif op==3:
            print(f"Multiplication of {round(num1)} and {round(num2)} is {round(num1*num2)}")
            if input("If you want value in decimal press Y else N: ")=='y'or'Y':
                print(f"Multiplication of {num1} and {num2} is {num1*num2}")
        elif op==4:
            print(f"Division of {round(num1)} and {round(num2)} is {round(num1/num2)}")           
            if input("If you want value in decimal press Y else N: ")=='y'or'Y':            
                print(f"Division of {num1} and {num2} is {num1/num2}")
        else:
            print("Invalid operation")
   
    elif op=='2':
        exp=input("Enter Valid expression: ")
       
        try:
            if '^' in exp:
                exp=exp.replace('^','**')
            if '//' in exp:
                exp=exp.replace('//','/')
            result=eval(exp) 
            print(f"\nResult of the expression {exp}:",round(result,2))
       
        except:
            print("\nInvalid expression")
   
    else:
        print("\nInvalid choice,Try again!")