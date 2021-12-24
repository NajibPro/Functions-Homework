def init (num1,num2,num):
    if (num >= num1 and num <= num2):
        print(num,"in range [",num1,",",num2,"]")
    elif (num >= num2 and num <= num1):
        print(num,"in range [",num2,",",num1,"]")
    else:
        if num2 >= num1:
             print(num,"isn't in range [",num1,",",num2,"]")
        else:
            print(num,"isn't in range [",num2,",",num1,"]")

init(input("give me the limits of your range first: "),input(),input("now give me a number: "))