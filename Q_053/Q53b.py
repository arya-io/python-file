# Assuming that we have some email addresses in the "username@companyname.com" format, 
# please write program to print the user name of a given email address. 
# Both user names and company names are composed of letters only.

# Example: If the following email address is given as input to the program:

# john@google.com
# Then, the output of the program should be:

# john

email = "john@google.com"
email = email.split('@')
print(email[0])