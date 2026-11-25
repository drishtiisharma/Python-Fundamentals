# for i in range(1,11):
#     print(i)

# i = 1
# while i < 11:
#     print(i)
#     i+=1

# for i in range(10,0,-1):
#     print(i)

# i = 10
# while i>=1:
#     print(i)
#     i-=1

# for i in range(1,51):
#     if i % 2 == 0:
#         print(i)


# even =  filter(lambda x : x % 2 == 0, range(1,51))
# print(list(even))

# odd = filter(lambda x : x %2 != 0, range(1,52))
# print((list(odd)))

# num = int(input("enter the number you'd like to see the table of: "))
# end = int(input("and till what range? "))
# for x in range(1,end+1):
#     print(num,"*",x,"=",num*x)


# end = int(input("cummulative sum till: "))
# sum = 0
# for x in range(1,end+1):
#     sum+=x

# print("cummulative sum till",end,":",sum)

# l=[]
# for i in range(1,101):
#     if i % 5 == 0:
#         l.append(i)
# print(l)

# num = int(input("enter number: "))
# l = []
# while num > 0:
#     digit = num % 10
#     l.append(digit)
#     num = num // 10
# l.reverse()
# print(l)

# num = int(input("enter num: "))
# count = 0
# while num > 0:
#     digit = num % 10
#     count += 1
#     num =  num // 10
# print(count)

# num = int(input("enter num: "))
# sum = 0
# while num > 0:
#     digit = num % 10
#     sum +=digit
#     num =  num // 10
# print(sum)