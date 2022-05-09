# scripted by samay 
# cybok hackers 
# cybok wars 
# advanse password generator !
# scripted in object oriented programming 

#----------------------imports ! 
import os
import sys
import random
import string
from os import system
from time import sleep

# --------------------colors 

r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"

#---------------------banners and tiny programs ! 
logo = """\033[1;37m

\033[1;37m[!] \033[1;31mThis is use for Password generator, You can Unlimitedly Edit !!! BYE :_)
\033[1;37m
┌-=============================   -   
=      \033[1;31m . ┌──────── \033[1;37mVaim-Samay    -   
=  \033[1;31m .┌───  \033[1;37mB-Hat Samay            -   \033[34m[✔]     https://github.com/samay825        [✔]
\033[1;37m=    Password Generator - Pro          -   \033[34m[✔]            Version 2.0                 [✔]
\033[1;37m= \033[1;31m . └──── \033[1;37mBY Samay               -   \033[91m[X] Please Don't Use For illegal Activity  [X]
\033[1;37m= \033[1;31m .     └─── \033[1;37mVERSION 2.0         -
\033[1;37m└-=============================   -

\033[1;31m    
Disclaimer: \033[1;32mthis tool is designed for Prank
	    testing in an authorized simulated cyberattack
	    Attacking targets without prior mutual consent
            is illegal!                                                               
\033[1;37m                                    
\033[97m """

#-------------------------bye functions 
def bye():
	os.system("clear")
	banner()
	string = """ 
	\033[1;37mDeveloper  \033[1;34m: \033[1;31mVAIM-SAMAY-VIRUSMAN

	\033[1;37mGithub     \033[1;34m: \033[1;31msamay825 & vaimpier_ritik

	\033[1;37mInstagram  \033[1;34m: \033[1;31moscp_samay__ & vaimpier_ritik

	\033[1;37mE-mail     \033[1;34m: \033[1;31mcybokhackers@gmail.com
	"""
	for letter in string:
	  sleep(0.01) 
	  sys.stdout.write(letter)
	  sys.stdout.flush()
	print("\n")

#-------------------------------------password generate
try:
   intpo = input(+g+"Press Enter : ")
except:
    pass
def returnfun():
    space()
    vaimsamay = input(r+"└─"+w+"\033[1;37mReturn back [y/n] : ")
    if vaimsamay=='Y' or vaimsamay=='y':
        return True
    elif vaimsamay=='N' or vaimsamay=='n':
        return False
    if vaimsamay:
        samay_repeat = Samay(intpo)
        samay_repeat.function_user()
    if vaimsamay==False:
        sys.exit()



    
def passwordgenerate(samay):
    try:
        vaimsamay = int(input(r+"└─"+w+"\033[1;37mEnter the length oF your Password : "+r))  # Enter the length oF your Password 
        space()
        empty_list = []
        samay_1 = string.ascii_lowercase
        samay_2 = string.ascii_uppercase
        samay_3 = string.punctuation
        samay_4 = string.digits
        empty_list.extend(samay_1)
        empty_list.extend(samay_2)
        empty_list.extend(samay_3)
        empty_list.extend(samay_4)
        random.shuffle(empty_list)
        samay_print = r+"└─"+w+"\033[1;37mThe Generated Password is == "+g+"".join(empty_list[0:vaimsamay])
        print(samay_print)
        if not os.path.exists(samay):
            os.makedirs(samay)
        with open(f'{samay}/{samay}.txt','w') as f:
            f.write(f"Password of YOur {samay} is "+"".join(empty_list[0:vaimsamay]))
        returnfun()
        space()
    except:
        space()
        print(r+"└─"+w+"\033[1;37mPlease restart program or put the numbers not string ! ")
        space()
        sys.exit()
        


#---------------------------------------------

def banner():
    print(logo)

def space():
    print('\n')

def options():
    system('clear')
    banner()
    space()
    print(r+"└─"+w+"\033[1;37m[ 1 ] Password Generate : ")
    print(r+"└─"+w+"\033[1;37m[ 2 ] About me : ")
    print(r+"└─"+w+"\033[1;37m[ 3 ] Exit : ")
    space()

options()

#--------------------------object oriented programming ! 


class Samay:
    def __init__(self,user_input):
        self.user = user_input
    def function_user(self):
        if self.user==1:
            while True:
                try:
                    system('clear')
                    banner()
                    space()
                    print(r+"└─"+w+"\033[1;37m[ 1 ] Instagram : ")
                    print(r+"└─"+w+"\033[1;37m[ 2 ] Facebook : ")
                    print(r+"└─"+w+"\033[1;37m[ 3 ] Snapchat : ")
                    print(r+"└─"+w+"\033[1;37m[ 4 ] Gmail : ")
                    print(r+"└─"+w+"\033[1;37m[ 5 ] Exit : ")
                    space()
                    self.samay = int(input(r+"└─"+w+"\033[1;37mEnter the Platform Which You want : "+r))
                    if self.samay==1:
                        system('clear')
                        banner()
                        space()
                        passwordgenerate("Instagram")
                    elif self.samay==2:
                        system('clear')
                        banner()
                        space()
                        passwordgenerate("Facebook")
                    elif self.samay==3:
                        system('clear')
                        banner()
                        space()
                        passwordgenerate("Snapchat")
                    elif self.samay==4:
                        system('clear')
                        banner()
                        space()
                        passwordgenerate("Gmail")
                    else:
                        space()
                        print(r+"└─"+w+"\033[1;37mExiting....")
                        sys.exit()
                except Exception as vaimsamaymandirbikhari:
                    space()
                    print(r+"└─"+w+"\033[1;37mPlease restart program or put the numbers not string ! ")
                    sys.exit()
        elif self.user==2:
            bye()
            sys.exit()
        else:
            space()
            print(r+"└─"+w+"\033[1;37mExiting....")
            sys.exit()

        

user_input = int(input(r+"└─"+w+"\033[1;37mEnter the Desire Option : "+r))
dic_Samay = Samay(user_input)
dic_Samay.function_user()




