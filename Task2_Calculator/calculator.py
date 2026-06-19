while True:
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    try:
        choice=int(input("\nEnter your choice: "))
        if (choice==5):
            break        
        x=int(input("\nEnter the first number: "))
        y=int(input("Enter the second number: "))
        if (choice==1):
            print("Result: ",x+y)
        elif (choice==2):
            print("Result: ",x-y)
        elif (choice==3):
            print("Result: ",x*y)
        elif (choice==4):
            if (y==0):
                print("Cannot divide by zero.")
            else:
                print("Result: ",x/y)
        else:
            print("Invalid choice.")
            
    except:
        print("Enter a valid number.")