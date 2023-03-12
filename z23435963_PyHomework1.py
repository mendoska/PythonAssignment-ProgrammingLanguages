# print statements are commented out from testing as I went down

# #1
# print("Hello world") 
# #2
# age = 27 
# #3 
# print ("Hello World, I'm "+ str(age) +"today") 
# #4
# str = "hello world"
# print (str.upper())
# #5
# d= 1.23
# #6 
# a = 12
# b = a 
# #7
# a = "hey"
# c = a
# #8
# print(a,type(a))
# print (b,type(b))
# print (c,type(c))
# print (d,type(d))
# #9
# mytuple = ("pizza", "wings", "subs")
# print(mytuple)
# #10
# classes = {
#     "Principles of Software Engineering": "Dr. Huang",
#     "Principles of Programming Languages": "Dr. Huang",
#     "Full-Stack Web Development": "Dr. Jaramillo",
#     "Practical Aspects Modern Cryptography": "Dr. Nojoumian"
# }
# #11
# print(classes)
# print(mytuple)

#12
# the * is used to unpack the range into the list
whole = [*range(1,101)]
# print(whole)

# #13
# div2 =[]
# div3 = []
# div4 = []
# div5=[]

# #14

# for x in whole:
#     if (x % 2 == 0):
#         div2.append(x)
#     if (x%3 ==0):
#         div3.append(x)
#     if(x%4 == 0):
#         div4.append(x)
#     if (x%5 == 0):
#         div5.append(x)


# #15
# print (whole)
# print("div by 2: ",div2, "\n")
# print("div by 3 ",div3, "\n")
# print("div by 4: ",div4, "\n")
# print("div by 5: ",div5, "\n")

#16
divOver5 = []

#17
for x in whole:
    if (x%2 != 0 & x%3 != 0 & x%4 != 0 & x%5 !=0 ):
        divOver5.append(x)


#18
print(divOver5)