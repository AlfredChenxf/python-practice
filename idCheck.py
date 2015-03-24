__author__ = 'Alfred'

import string

alphas = string.letters + '_'
numbers = string.digits

print "First version for idCheck"

str = raw_input("Enter string:")

if len(str) > 1:
    if str[0] not in alphas:
        print "Invalid, not alphas"
    else:
        for otherChar in str[1:]:
            if otherChar not in alphas + numbers:
                print "Invalid, not alphas + numbers"
                break
        else:
            print "Valid identifier"