# Write a program which accepts a string as input to 
# print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

x = str(input().lower())
if x == 'yes':
    print('Yes')
else:
    print('No')