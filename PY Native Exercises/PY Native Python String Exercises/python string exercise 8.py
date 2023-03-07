#Write a program to find all occurrences of “USA” in a given string ignoring the case.

str1 = "Welcome to USA. usa awesome, isn't it? Yay, UsA"

def my_function():
    str2 = str1.lower()
    #usacountupper = str1.count("USA") 
    usacountlower = str2.count("usa")
    usacount = usacountlower 
    print(("The USA count is: {}.").format(usacount))

my_function()
