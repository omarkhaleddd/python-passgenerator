import os
import string
import random
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

passwordno = input("Enter number of charaters the password would be : ")
#to check on the passno is more than 6 and it is number
while True:
    try:
        passwordno = int(passwordno)
        if passwordno < 6:
            print("number of characters must be at least 6")
            passwordno = input("\nenter number of characters again : ")
        else:
            break
    except:
        print("enter numbers only")
        passwordno = input("\nenter number of characters again : ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)
part1 = round(passwordno * 30/100)
part2 = round(passwordno * 20/100)

password = []
for i in range(part1):
    password.append(s1[i])
    password.append(s2[2])
for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)
password = "".join(password[0:])
filename = "passwords.txt"

if os.path.exists(filename):
    append_write = 'a' # append if already exists
else:
    append_write = 'w' # make a new file if not

f = open("passwords.txt" ,append_write)
f.write("password : " + str(password) + "\n")
f.close()
print (password)

