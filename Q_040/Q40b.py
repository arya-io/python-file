# Write a program which accepts a string as input to 
# print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

text = input("Please type something. --> ")
if text == "yes" or text == "YES" or text == "Yes":
    print("Yes")
else:
    print("No")