def pr (num):
    i = 2
    if num == 0 or num == 1 or num == -1 :
        print(num,"is not prime")
    else:
        while (i <= num // 2 and num > 2) or (i <= -num // 2 and num < -2) :
            if num % i != 0 :
                i += 1
            else :
                print(num ,"is not prime")
                break
        else :
            print(num,"is prime")

pr(int(input("enter your number: ")))