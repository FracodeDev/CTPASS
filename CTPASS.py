import os
import sys
from colorama import Fore,Style
import random as rnd
from random import randint
import time
from lib.display import banner_passls
from lib.prj1_passList import passls1 , passls2 , passls3
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
AND="and"
A=""
#####all color code#####
black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
lightgrey = '\033[37m'
darkgrey = '\033[90m'
lightred = '\033[91m'
lightgreen = '\033[92m'
yellow = '\033[93m'
lightblue = '\033[94m'
pink = '\033[95m'
lightcyan = '\033[96m'
Blue='\033[1;34m'
Green="\033[1;33m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
#####################
def banner():  
    # multi printer <== made banner for script 
    print(Fore.LIGHTRED_EX,"")
    print("  ______         _______      _________      ________")  
    print(" / ____/        |  _____|    |_________|    |#      *\ ") 
    print(" \ ____\    =   | |              | |        |# _____*/ ") 
    print(" /  ___/    =   | |_____         | |        |#|_____") 
    print(" \ ____\        |_______|        | |        |#      *\ ")
    print("  <++++>        {/*/*/*/}        |_|        |#______*/ ")
banner()
def print_t():
    print("                                        ") 
print_t()
def print_DU():
    print_t()
    print_t()
def addLS():
    ls=[]
    QU=int(input("Enter number :"))
    print("                       ")
    for i in range(QU):
        a=input("Enter Name :")
        ls.append(a)
    print(ls)
__version__="v1.2.8T"
while True:
    def timercock(t):
    
        while(t>=0):
            mins,secs=divmod(t,60)

            hrs,mins=divmod(mins,60)

            timer='{:02d} : {:02d} :{:02d}'.format(hrs,mins,secs)

            print(Fore.MAGENTA,Style.BRIGHT,timer, end="\r")
            time.sleep(1)
            t-=1
    t=3
    timercock(t)
    def usage():
        print(Fore.BLUE,"================================================================")
        print(Fore.BLUE,Style.BRIGHT," Usage : CTPASS <options> ")
        print_t()
        print(Fore.GREEN,Style.BRIGHT,f" Name : CTPASS ==> city Password   version :{__version__}")
        print_t()
        print(Fore.YELLOW,Style.BRIGHT," Options:                          ")
        print_t()
        print("    {1} --help         help in program and show usage")
        print("    {2} --operation    perform the operation of creating a password list")
        print("    {3} --password     creat a security password")
        print("    {4} --quastion     Explanation of the questions of this program")
        print("    {5} --version      type version program                ")
        print("    {6} --encrip       one allgoritm encrypted and ")
        print("    {0} --exit         Exit the program CTPASS             ")
        print_t()
        print(" ================================================================")
        print_t()
        print(Fore.RED,"[\]CTPASS~#:",end=" ")
        global A
        A=input()
    usage()
    if(A=="1"):
        continue
    elif(A=="2"):
        os.system("clear")
        banner_passls()
        def slowprint(s):
	          for c in s + '\n' :
                      sys.stdout.write(c)
                      sys.stdout.flush()
                      time.sleep(10/100)
        print_t()
        slowprint("\033[91m[+]python script CTPASS...")
        slowprint("\033[92m[+]runing password list program...")
        slowprint("\033[97m[+]update script CTPASS...")
        slowprint("\033[95m[+]password list creating operation...")
        time.sleep(0.5)
        os.system('cls')
        print(blue,"")
        banner_passls()
        print(orange,'[',blue,'FOLLOW ON INSTAGRAM :- @CODER.FIXED',orange,']')
        print_t()
        print(orange,'+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ >>')
        print(cyan,'|S|C|R|I|P|T| |C|T|P|A|S|S| |F|O|R| |P|A|S|S|L|S|')
        print(orange,'+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ >>')
        print_t()
        slowprint('\033[92m[1]-[Creating a \033[91mPassword list[ Atoumatic ]\033[97mFOR : wordpress , instagram , Brute Force ...]')
        print_t()
        slowprint('\033[97m[2]-[Creating a \033[93mPassword list[ Manually  ]\033[91mFOR : wordpress , instagram , Email , Brute Force ...]')
        print_t()
        slowprint('\033[93m[3]-[Image \033[97mEncryption [ Manually ]\033[92mFOR : Imgaes ...]')
        print_t()
        print(Fore.RED,"[/]CTPASS[LIST]~#:",end=" ")
        B = input()
        if B == '1':
            slowprint('\033[97mWelcome you!')
            print('Enter number of min size : ' , end = " ")
            Min = int(input())
            print('Enter number of max size : ' , end = " ")
            Max = int(input())
            print('Enter number of the range : ' ,end = " ")
            Self = int(input())
            passls1(Min , Max , Self)
            print('create file password list [yes or no] ? ' ,end = " ")
            QUS = input()
            if QUS == 'yes' :
                print(Fore.GREEN,"  [+]",Fore.MAGENTA,"Enter name file text ~$ ",end="")
                NFile=input()
                FILE=open(f"pass_file/{NFile}","w")
                print_t()
                print(Fore.GREEN," [ The file was created ]")
            else :
                break
            os.system('cls')
        elif B == '2':
            slowprint('\033[97mWelcome you!')
            print('Enter number of min size : ' , end = " ")
            Min = int(input())
            print('Enter number of max size : ' , end = " ")
            Max = int(input())
            print('Enter number of the range : ' ,end = " ")
            Self = int(input())
            passls2(Min , Max , Self)
            print('create file password list [yes or no] ? ' ,end = " ")
            QUS = input()
            if QUS == 'yes' :
                print(Fore.GREEN,"  [+]",Fore.MAGENTA,"Enter name file text ~$ ",end="")
                NFile=input()
                FILE=open(f"pass_file/{NFile}","w")
                print_t()
                print(Fore.GREEN," [ The file was created ]")
            else :
                break
            os.system('cls')
        elif B == '3':
            slowprint('\033[97mWelcome you!')
            print('Enter number of min size : ' , end = " ")
            Min = int(input())
            print('Enter number of max size : ' , end = " ")
            Max = int(input())
            print('Enter number of the range : ' ,end = " ")
            Self = int(input())
            passls3(Min , Max , Self)
            print('create file password list [yes or no] ? ' ,end = " ")
            QUS = input()
            if QUS == 'yes' :
                print(Fore.GREEN,"  [+]",Fore.MAGENTA,"Enter name file text ~$ ",end="")
                NFile=input()
                FILE=open(f"pass_file/{NFile}","w")
                print_t()
                print(Fore.GREEN," [ The file was created ]")
            else :
                break
            os.system('cls')
    elif(A=="3"):
        def slowprint(s):
	        for c in s + '\n' :
                 sys.stdout.write(c)
                 sys.stdout.flush()
                 time.sleep(10/150)
        os.system("cls")
        slowprint("\033[91m[+]python script CTPASS...")
        slowprint("\033[97m[+]creat a security password...")
        slowprint("\033[95m[+]choose a password level...")
        slowprint("\033[91m[+]password creating operation...")
        print(Fore.GREEN,"                                                               ")
        print("[+]Choose a password level /~",end=" ")
        print("{1}Normal  {2}Strong  {3}security")
        print_t()
        L=input("[\]CTPASS~#: ")
        timercock(t)
        if(L=="Normal" or L=="1"):
            print_t()
            print(Fore.GREEN,"  [+]",Fore.BLUE,"what is your name",Fore.RED,end="~#: ")
            n1=input()
            n2=n1[:4]
            print_DU()
            print(Fore.GREEN,"  [+]",Fore.BLUE,"what is your last name",Fore.RED,end="~#: ")
            ln1=input()
            ln2=ln1[::3]
            ln1=ln1[:1]
            print_DU()
            print(Fore.GREEN,"  [+]",Fore.BLUE,"What is your birth year",Fore.RED,end="~#: ")
            Y1=int(input())
            x2=Y1
            print_t()
            x1=Y1-1402
            x1-=x1+x1
            print_t()
            print(Fore.GREEN,"  [+]",Fore.MAGENTA,"Enter name file text ~$ ",end="")
            NFile=input()
            FILE=open(f"pass_file/{NFile}","w")
            print_t()
            print(Fore.GREEN," [ The file was created ]")
            print_t()
            print(Fore.GREEN,"   *******************")
            print(Fore.GREEN,"    ","1.",'{}{}{}'.format(n2,ln1,x1))
            print(Fore.GREEN,"    ","2.",'{}{}{}'.format(n1,ln1,x2))
            print(Fore.GREEN,"    ","3.",'{}{}{}'.format(n2,x1,ln2))
            print(Fore.GREEN,"   *******************") 
            Vw1=n2+ln1+str(x1)
            Vw2=n1+ln1+str(x2)
            Vw3=n2+str(x1)+ln2
            FILE.write(Vw1)
            FILE.write('\n')
            FILE.write(Vw2)
            FILE.write('\n')
            FILE.write(Vw3)
            FILE.close()
        elif(L=="Strong" or L=="2"):
            print_t()
            print(Fore.GREEN," [+]",Fore.BLUE,"what is your name",Fore.RED,end="~#: ")
            n3=input()
            n4=n3[:6:2]
            print_DU()
            print(Fore.GREEN," [+]",Fore.BLUE,"what is your last name",Fore.RED,end="~#: ")
            ln3=input()
            ln4=ln3[:4]
            ln5=ln3[:1]
            print_DU()
            print(Fore.GREEN," [+]",Fore.BLUE,"What is your birth year",Fore.RED,end="~#: ")
            Y2=int(input())
            Y3=Y2-1402
            Y3-=Y3+Y3
            print_DU()
            print(Fore.GREEN," [+]",Fore.BLUE,"What is your father's name",Fore.RED,end="~#: ")
            FN1=input()
            FN2=FN1[:1]
            print_DU()
            print(Fore.GREEN," [+]",Fore.BLUE,"What is your mobile number",Fore.RED,end="~#: ")
            NM1=input()
            NM2=NM1[8::]
            NM3=NM1[9:]
            print_DU()
            print(Fore.GREEN," [+]",Fore.BLUE,"The name of one of your friends",Fore.RED,end="~#: ")
            NMF1=input()
            print_t()
            ls1=["!","?"]
            SX=rnd.choice(ls1)
            ls2=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","T","R","S","U","W","X","Y","Z"]
            SX1=rnd.choice(ls2)
            print_t()
            print(Fore.GREEN," [+]",Fore.MAGENTA,"Enter name file text ~$ ",end="")
            NFile1=input()
            FILE1=open(f"pass_file/{NFile1}","w")
            print_t()
            print(Fore.GREEN," [ The file was created ]")
            print_t()
            print(Fore.YELLOW,"   ************************")
            print(Fore.YELLOW,"    ","1.","{}{}{}{}{}".format(n4,Y3,ln4,NM2,FN2))
            print(Fore.YELLOW,"    ","2.","{}{}{}{}{}".format(NMF1,SX1,ln5,n3,Y2))
            print(Fore.YELLOW,"    ","3.","{}{}{}{}{}".format(SX,n3,Y3,FN2,NM3))
            print(Fore.YELLOW,"    ","4.","{}{}{}{}{}".format(SX1,n4,NM2,SX,Y2))
            print(Fore.YELLOW,"    ","5.","{}{}{}{}{}".format(SX1,SX,n3,Y3,NM3))
            print(Fore.YELLOW,"    ","6.","{}{}{}{}{}".format(FN1,SX,ln5,Y2,NM2))
            print(Fore.YELLOW,"   ************************")
            Vw4=n4+str(Y3)+ln4+NM2+FN2
            Vw5=NMF1+SX1+ln5+n3+str(Y2)
            Vw6=SX+n3+str(Y3)+FN2+NM3
            Vw7=SX1+n4+NM2+SX+str(Y2)
            Vw8=SX1+SX+n3+str(Y3)+NM3
            Vw9=FN1+SX+ln5+str(Y2)+NM2
            FILE1.write(Vw4)
            FILE1.write('\n')
            FILE1.write(Vw5)
            FILE1.write('\n')
            FILE1.write(Vw6)
            FILE1.write('\n')
            FILE1.write(Vw7)
            FILE1.write('\n')
            FILE1.write(Vw8)
            FILE1.write('\n')
            FILE1.write(Vw9)
            FILE1.close()
        elif(L=="security" or L=="3"):
            print_t()
            print(Fore.RED," [-]",Fore.CYAN,"what is your name",Fore.RED,end="~#: ")
            n5=input()
            n6=n5[:4]
            n7=n5[::2]
            n8=n5[:1]
            print_DU()
            print(Fore.RED," [-]",Fore.CYAN,"what is your last name",Fore.RED,end="~#: ")
            ln6=input()
            ln7=ln6[:1]
            ln8=ln6[:2]
            ln9=ln6[6:]
            print_DU()
            print(Fore.RED," [-]",Fore.CYAN,"What is your birth year",Fore.RED,end="~#: ")
            Y4=int(input())
            Y5=Y4-1402
            Y5-=Y4+Y4
            print_DU()
            print(Fore.RED," [-]",Fore.CYAN,"What is your father's name",Fore.RED,end="~#: ")
            FN3=input()
            FN4=FN3[:1]
            FN5=FN3[::2]
            FN6=FN3[:4]
            print_DU()
            print(Fore.RED," [-]",Fore.CYAN,"What is your mobile number",Fore.RED,end="~#: ")
            NM4=input()
            NM5=NM4[9:]
            NM6=NM4[7:]
            NM7="+98"
            print_DU()
            print(Fore.RED," [-]",Fore.CYAN,"The name of one of your friends",Fore.RED,end="~#: ")
            NMF2=input()
            NMF3=NMF2[:3]
            NMF4=NMF2[:1]
            print_DU()
            print(Fore.RED," [-]",Fore.CYAN,"What is your national code",Fore.RED,end="~#: ")
            NASHCODE1=input()
            NASHCODE2=NASHCODE1[:3]
            NASHCODE3=["28","09"]
            SX6=rnd.choice(NASHCODE3)
            print_DU()
            print(Fore.RED," [-]",Fore.CYAN,"What is your mobile operating system",Fore.RED,end="~#: ")
            SYSMOBILE1=input()
            SYSMOBILE2=SYSMOBILE1[:5]
            SYSMOBILE3=SYSMOBILE1[4:]
            print_DU()
            print(Fore.RED," [-]",Fore.CYAN,"What is your favorite sport",Fore.RED,end="~#: ")
            FAVSPORT=input()
            st3={"wushu","Soccer","Chess","Box","UFC","MMA","KungFu","basketball",
                 "tennis","Ping pong","Karate"}
            if(FAVSPORT in st3):
                FAVSPORT="*"+FAVSPORT
            else:
                FAVSPORT=FAVSPORT
            print_DU()
            print(Fore.RED," [-]",Fore.CYAN,"What is your mother's name",Fore.RED,end="~#: ")
            MN1=input()
            MN2=MN1[:1]
            print_DU()
            print(Fore.RED," [-]",Fore.CYAN,"What is your nickname",Fore.RED,end="~#: ")
            NICE1=input()
            print_DU()
            print(Fore.RED," [-]",Fore.CYAN,"what is your country",Fore.RED,end="~#: ")
            nCONTRY1=input()
            if(len (nCONTRY1)<4):
                nCONTRY3=nCONTRY1[:3]
            else:
                nCONTRY2=nCONTRY1[:2]
            print_DU()
            Ls3=["@","#","$","%","^","&"]
            SX2=rnd.choice(Ls3)
            Ls4=["admin","user","hacker","king","nice","Wolf","Leon","supper"]
            SX3=rnd.choice(Ls4)
            TP1=set()
            TP2=set()
            for i in range(5):
                TP1.add(randint(1,20))
                TP2.add(randint(1,9))
            #=================================
            print(Fore.GREEN," [+]",Fore.MAGENTA,"Enter name file text ~$ ",end="")
            NFile2=input()
            FILE2=open(f"pass_file/{NFile2}","w")
            print_t()
            print(Fore.GREEN," [ The file was created ]")
            print_t()
            print(Fore.GREEN,"   *****************************")
            print(Fore.GREEN,"    ","1.","{}{}{}{}{}{}".format(n6,SX3,FAVSPORT,SX2,NM5,ln8))
            print(Fore.GREEN,"    ","2.","{}{}{}{}{}{}".format(SX3,SX2,FAVSPORT,SYSMOBILE2,MN2,NICE1))
            print(Fore.GREEN,"    ","3.","{}{}{}{}{}{}".format(SX2,SX6,FN4,NM5,n6,SX2))
            print(Fore.GREEN,"    ","4.","{}{}{}{}{}{}".format(n6,SX3,nCONTRY2,FAVSPORT,SYSMOBILE2,NMF4))
            print(Fore.GREEN,"    ","5.","{}{}{}{}{}{}".format(NM7,FN4,ln8,n8,Y5,NICE1))
            print(Fore.GREEN,"    ","6.","{}{}{}{}{}{}".format(n8,FN4,MN2,NASHCODE1,NM5,NMF3))
            print(Fore.GREEN,"    ","7.","{}{}{}{}{}{}".format(NICE1,SX2,NASHCODE2,ln8,SX6,MN2))
            print(Fore.GREEN,"    ","8.","{}{}{}{}{}{}".format(FAVSPORT,ln8,MN2,SX6,NM5,SX3))
            print(Fore.GREEN,"    ","9.","{}{}{}{}{}{}".format(SYSMOBILE2,n8,NICE1,NASHCODE2,SX2,n6))
            print(Fore.GREEN,"    ","A.","{}{}{}{}{}{}".format(NMF4,SX6,Y5,NICE1,ln8,nCONTRY2))
            print(Fore.GREEN,"    ","B.","{}{}{}{}{}{}".format(nCONTRY2,Y5,MN2,n8,n6,SX3))
            print(Fore.GREEN,"    ","C.","{}{}{}{}{}{}".format(SX2,NICE1,FN4,n8,ln8,SX2))
            print(Fore.GREEN,"   *****************************")
            Vw10=n6+SX3+FAVSPORT+SX2+NM5+ln8
            Vw11=SX3+SX2+FAVSPORT+SYSMOBILE2+MN2+NICE1
            Vw12=SX2+SX6+FN4+NM5+n6+SX2
            Vw13=n6+SX3+nCONTRY2+FAVSPORT+SYSMOBILE2+NMF4
            Vw14=NM7+FN4+ln8+n8+str(Y5)+NICE1
            Vw15=n8+FN4+MN2+NASHCODE1+NM5+NMF3
            Vw16=NICE1+SX2+NASHCODE2+ln8+SX6+MN2
            Vw17=FAVSPORT+ln8+MN2+SX6+NM5+SX3
            Vw18=SYSMOBILE2+n8+NICE1+NASHCODE2+SX2+n6
            Vw19=NMF4+SX6+str(Y5)+NICE1+ln8+nCONTRY2
            Vw20=nCONTRY2+str(Y5)+MN2+n8+n6+SX3
            Vw21=SX2+NICE1+FN4+n8+ln8+SX2
            FILE2.write(Vw10),FILE2.write('\n'),
            FILE2.write(Vw11),FILE2.write('\n'),
            FILE2.write(Vw12),FILE2.write('\n'),
            FILE2.write(Vw13),FILE2.write('\n'),
            FILE2.write(Vw14),FILE2.write('\n'),
            FILE2.write(Vw15),FILE2.write('\n'),
            FILE2.write(Vw16),FILE2.write('\n'),
            FILE2.write(Vw17),FILE2.write('\n'),
            FILE2.write(Vw18),FILE2.write('\n'),
            FILE2.write(Vw19),FILE2.write('\n'),
            FILE2.write(Vw20),FILE2.write('\n'),
            FILE2.write(Vw21),FILE2.write('\n')
            FILE2.close()
    elif(A=="4"):
        os.system("cls")
    elif(A=="5"):
        timercock(t)
        def version():
            print(Fore.BLACK,f"  version :{__version__}")
        version()
    elif(A=="6"):
        while True :
           print("                                                              ")
           print(Fore.RESET,"=========================================================")
           print(" Choose a options :",end=" ")
           print(Fore.RED,"{1}Encrypted(1) {2}Decrypted(1) {3}Encrypted(2) {4}Decrypted(2) {5}EXIT")
           print(Fore.RESET,"=========================================================")
           BP=input("[\]CTPASS~#: ")
           AB=''
           if(BP=="1"):
               print(Fore.GREEN,"                                                 ")
               message = input(" Write the text :") #encrypted message
               LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
               for key in range(len(LETTERS)):
                   translated = ''
                   for symbol in message:
                       if (symbol in LETTERS):
                          num = LETTERS.find(symbol)
                          num = num - key
                          if (num < 0):
                             num = num + len(LETTERS)
                          translated = translated + LETTERS[num]
                       else:
                          translated = translated + symbol
               AB=translated
               massage1=AB
               translate1=''
               i1=len(massage1)-1
               while i1 >=0:
                   translate1=translate1+massage1[i1]
                   i1=i1-1
               time.sleep(1)
               print(Fore.BLUE,"[                    ] 0% ")
               time.sleep(1)
               print(" [=====               ] 25%")
               time.sleep(1)
               print(" [==========          ] 50%")
               time.sleep(1)
               print(" [===============     ] 75%")
               time.sleep(1)
               print(" [====================] 100%")
               time.sleep(1)
               print(Fore.MAGENTA,"  [ TEXT ENCRYPTED ]")
               print(Fore.RED,'Hacking key #%s: %s' % (key, translate1))
           elif(BP=="2"):
               print(Fore.GREEN,"                                                 ")
               my_string=input(" write the text ~#:")
               reversed_string=""
               for char in my_string:
                   reversed_string=char+reversed_string
               XY=reversed_string
               message2=XY
               LETTERS2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
               for key2 in range(len(LETTERS2)):
                   translated2=''
                   for symbol2 in message2:
                     if(symbol2 in LETTERS2):
                       num2=LETTERS2.find(symbol2)
                       num2=num2 + key2
                       if(num2 > 0):
                           num2=num2 - len(LETTERS2)
                       translated2=translated2+LETTERS2[num2]
                     else:
                       translated2=translated2 - symbol2
               time.sleep(1)
               print(Fore.BLUE,"[                    ] 0% ")
               time.sleep(1)
               print(" [=====               ] 25%")
               time.sleep(1)
               print(" [==========          ] 50%")
               time.sleep(1)
               print(" [===============     ] 75%")
               time.sleep(1)
               print(" [====================] 100%")
               time.sleep(1)
               print(Fore.MAGENTA,"  [ TEXT ENCRYPTED ]")
               print(Fore.RED,'Hacking Encrypted #%o: %s' % (key2, translated2))
           elif(BP=="3"):
               print(Fore.GREEN,"                                                 ")
               message_string=input(" write the text ~#:")
               # تولید یک جفت کلید RSA
               private_key = rsa.generate_private_key(
                   public_exponent=65537,
                   key_size=2048
               )
               public_key = private_key.public_key()

               # متنی برای رمزنگاری
               message = b'Alireza Mirzaei'
               # رمزنگاری پیام با استفاده از کلید عمومی
               ciphertext = public_key.encrypt(
                   message,
                   padding.OAEP(
                       mgf=padding.MGF1(algorithm=hashes.SHA256()),
                       algorithm=hashes.SHA256(),
                       label=None
                   )
                )
               # نمایش متن رمزنگاری شده
               time.sleep(1)
               print(Fore.BLUE,"[                    ] 0% ")
               time.sleep(1)
               print(" [=====               ] 25%")
               time.sleep(1)
               print(" [==========          ] 50%")
               time.sleep(1)
               print(" [===============     ] 75%")
               time.sleep(1)
               print(" [====================] 100%")
               time.sleep(1)
               print(Fore.MAGENTA,"  [ TEXT ENCRYPTED ]")
               print(Fore.RED,'Hacking Encrypted #: ', ciphertext)
    elif(A=="clear"):
        os.system("cls")
    elif(A=="0"):
        timercock(t)
        print_t()
        print(Fore.BLUE,"Do you want to exit ~$",end=" ")
        E=input()
        if(E=="yes"):
            print_t()
            print(Fore.RED,"[ Exit the program ]")
            print_t()
            sys.exit()
        else:
            print_t()
            continue