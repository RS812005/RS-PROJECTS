import random
import string
import time

red="\33[31m"
green="\33[32m"
default="\33[0m"

inp=input("Enter your massage :")
choice=int(input("\nEnter 1 to code your massage into secret code Or\nEnter 0 to decode the secred code :"))
inp=inp.split()
inpn=[]
coding=True if (choice==1) else False
if (coding):
    print(f"\n{red}coding{default}")
    time.sleep(2)
    for i in inp:
        def creat_random_string(length):
            letters=string.ascii_lowercase+string.ascii_uppercase+string.punctuation+string.digits
            rs="".join(random.choice(letters) for i in range(length))
            return rs
        newrs=creat_random_string(3)
        newrs1=creat_random_string(3)                       
        if len(i)>=3:
            i=newrs+i[1:]+i[0]+newrs1
            inpn.append(i)
        elif len(i)<=2:
            i=i[::-1]
            i=newrs+i+newrs1
            inpn.append(i)
        massage=" ".join(inpn)    
    print(f"here is your massage:\n{massage}")
else:
    print(f"\n{green}decoding{default}")
    time.sleep(2)
    for i in inp:
        if len(i)>=3:
            i=i[3:-3]
            i=i[-1]+i[:-1]
            inpn.append(i)
        elif len(i)<=2:
            i=i[::-1]
            i=i[3:-3]
            inpn.append(i)
        massage=" ".join(inpn)
    print(f"here is your massage:\n{massage}")