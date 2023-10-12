while(True):
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    welcomemsg='''====Welcome to my calculator====
    Please enter the choice
    1.To Add numbers
    2.To Sub numbers
    3.To multiply numbers
    4.To divide numbers
    5.To exit the calculator '''
    print(welcomemsg)
    c=int(input("Enter the your choice:"))
    if c==1:
        sum=a+b
        print(f"The addition of two number is {sum}.")
    if c==2:
        sub=a-b
        print(f"The subtraction of two number is {sub}.")
    if c==3:
        multi=a*b
        print(f"The multiply of two number is {multi}.")
    if c==4:
        if b==0:
            print("Infinite")
            break
        div=a/b
        print(f"The divide of two number is {div}.")
    if c==5:
        print("Thanks for using calculator!")
        break