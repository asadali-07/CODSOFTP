import string

import random

s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4=string.punctuation

s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

random.shuffle(s)

passlen=int(input("Enter the password length:"))

print("Your generated password is:")

# print("".join(random.sample(s,passlen))) if we wnat use we dont to suffle the list!

print("".join(s[0:passlen]))