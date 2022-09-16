# 1. Write a python script to create a String in 3 different possible ways
string1='jyoti'
string2="Jyoti"
string3='''JYOTI'''
print(string1,string2,string3,sep=" ")
print()

# 2. Write a python script to Get the characters from the start to position 5 (Given String “iNeuron” using the slice syntax)
string=input("Enter given string.")
print("the characters from the start to position 5",string[:6:1])
print()

# 3. Write a python script to Get the characters from position 2 to position 5 (Given String “Hello Learners” using the slice syntax)
string=input("Enter given string.")
print("the characters from the position 2 to position 5",string[2:6:1])
print()

# 4. Write a python script to demonstrate String Concatenation adding space in between ( Given Strings a=”Learning” b=”Python” )
a="Learning"
b="Python"
print(a+" "+b)
print()

# 5. Write a python script to get the count of total number of characters in String a= “iNeuron”
string="iNeuron"
count=0
for i in string:
    count+=1
print("total number of character in iNeuron",count)    
print()

# 6. Write a python script to reverse a String. (“iNeuron”)
string="iNeuron"
print("Reverse a string iNeuron is ",string[::-1])
print()

# 7. Write a python script to determine whether a string contains a specific substring.
string1=input("Enter any string ")
sub_string=input("Enter any substring..")
if sub_string in string1:
    print(sub_string,"Sub_string is found in string",string1)
else:
    print("No its not substring")    
print()

# 8. Write a python script to check if a string contains only numbers.
string=input("Enter string ")
print(string," string contains only number. ",string.isnumeric())
print()

# # 9. Write a python script to check if a string contains only characters of the alphabet.
string=input("Enter string ")
print(string," string contains only characters of the alphabet. ",string.isalpha())
print()

# 10. Write a python script to convert an integer to a string
num=int(input("Enter number"))
string=str(num)
print(num," given number whose string is ",string,type(string),sep=" ")