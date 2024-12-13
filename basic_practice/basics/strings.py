
#string are immutable --> important point 
name = "bidur"

# replace 
name.replace("bidur_poudel", "bidur Poudel")

index_name = name[1:4]
# [index_start(includes): index_end(not include)] 
print(index_name)

#print 3rd index of name 
char_name = name[3] 


#gives total numbers of character in string
print(len(name)) 

#gives boolean value if given word is present in string
print(name.endswith("ur")) 

#gives boolean value if give word is started word or not ....
print(name.startswith("d")) 


# Removes leading and trailing characters (default is whitespace)
print(' hello '.strip()) #output: 'hello'

# Swaps the case of all characters in the string.
print("Hello World".swapcase())  # Output: 'hELLO wORLD'


print("hello world".title()) #output: "Hello World"

print("hello".upper())  # Output: 'HELLO'

print("42".zfill(5))  # Output: '00042'


