#Enter Python code here and hit the Run button.
str1 = "P@#yn26at^&i5ve"
#Count all letters, digits,
#and special symbols from a given string

letters = [i for i in str1 if i.isalpha() == True]
numbers = [i for i in str1 if i.isnumeric() == True]
symbols = [i for i in str1 if i.isalpha()!= True and i.isnumeric() != True]
        
print ("There are {} letters, {} numbers, and {} symbols.".format(len(letters), len(numbers), len(symbols)))



