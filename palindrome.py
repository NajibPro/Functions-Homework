def paly (word):
 b = True
 first = 0
 last = len(word) - 1
 while(first <= last):
     while word[first] == " ":
         first += 1
     while word[last] == " ":
         last -= 1
     if word[first] == word[last]:
         first += 1
         last -= 1
     else:
         b = False
         break
 if b :
     return print(word ,"is a palindrom string")
 else:
     return print(word ,"is not a palindrome string")


paly(input("please enter a string"))