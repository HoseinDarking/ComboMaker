# Jailbreak & Root
# jilrot.com
# t.me/jailbreakandroot
# -- Combo List Maker --
import time, os

os.system("clear")
userf = input("Username File: ")
passf = input("Password File: ")
usrf = open(userf, "r").read().splitlines()
pasf = open(passf, "r").read().splitlines()

userlist = []
passlist = []

os.system("clear")
print ('\n'+"      - Loading Data ...")
time.sleep(3)

for u in usrf:
    userlist.append(u.replace('\n',""))

for p in pasf:
    passlist.append(p.replace('\n',""))

os.system("clear")
print ('\n'+"      - Combo List Makeing ...")
time.sleep(3)

combof = open("combolist.txt","a")

if len(userlist) > len(passlist):
    for num in range(len(passlist)):
        username = userlist[num]
        password = passlist[num]
        combo = username+":"+password
        combof.write(combo+'\n')
        print (combo)

elif len(userlist) < len(passlist):
    for num in range(len(userlist)):
        username = userlist[num]
        password = passlist[num]
        combo = username+":"+password
        combof.write(combo+'\n')
        print (combo)

if len(userlist) == len(passlist):
    for num in range(len(passlist)):
        username = userlist[num]
        password = passlist[num]
        combo = username+":"+password
        combof.write(combo+'\n')
        print (combo)
combof.close()

os.system("clear")
print ('\n'+"      - Combo List Maked ;")
