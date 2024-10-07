import customtkinter
from colorama import Fore
from random import randint , randrange , choice
import tkinter
import mysql.connector as mc
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

page_1 = customtkinter.CTk()
page_1.geometry('485x500')
page_1.minsize(width=485 , height=500)
page_1.maxsize(width=485 , height=500)
page_1.title('xCTPASS')
  
def button_Login_function_usage():
    user_name = username.get()
    pass_word = password.get()
    check = check_robot.get()
    GENDER = gender.get()
    if user_name == '1' and pass_word == '11':
        if check == 1:
            page_1.destroy()
            page_2 = customtkinter.CTk()
            page_2.geometry('745x480')
            page_2.title('home page')
            page_2.minsize(width=745 , height=480)
            page_2.maxsize(width=745 , height=480)
            lb_xCTPASS = customtkinter.CTkLabel(master=page_2 , text=f'xCTPASS : {__version__}', font=('Arial',15),text_color='red')
            lb_xCTPASS.place(x = 10,y=8)
            lb_user = customtkinter.CTkLabel(master=page_2 , text=f'USERNAME  : {user_name}' , font=('Arial',15),text_color='green')
            lb_user.place(x=10,y=35)
            HIDE_PASS_lEN= len(pass_word)
            HIDE_PASS=''
            for i in range(HIDE_PASS_lEN):
                HIDE_PASS+='*'
            lb_pass = customtkinter.CTkLabel(master=page_2 , text=f'PASSWORD : {HIDE_PASS}', font=('Arial',15),text_color='green')
            lb_pass.place(x=10 , y=63)
            BTN_help = customtkinter.CTkButton(master=page_2 , text='Help', width=100 ,hover_color='#009eff' , text_color='black' , fg_color='#00ffff')
            BTN_help.place(x=640 , y=8)
            page_2.mainloop()
def button_SING_function_usage():
    page_3 = customtkinter.CTk()
    page_3.geometry('485x500')
    page_3.minsize(width=485 , height=500)
    page_3.maxsize(width=485 , height=500)
    page_3.title('xCTPASS')

    frame1 = customtkinter.CTkFrame(master=page_3 , width=340 , height=420)
    frame1.place(x=75,y=45)

    title1 = customtkinter.CTkLabel(master=frame , text=f'Create a account {__xCTPASS__}' ,font=('Arial',20))
    title1.place(x=30,y=30)
    page_3.mainloop()
__version__="v1.2.8T"   
__xCTPASS__ ='xCTPASS'
frame = customtkinter.CTkFrame(master=page_1 , width=340 , height=420)
frame.place(x=75,y=45)

title = customtkinter.CTkLabel(master=frame , text=f'Login to the account {__xCTPASS__}' ,font=('Arial',20))
title.place(x=30,y=30)

username = customtkinter.CTkEntry(master=frame , width=220 , placeholder_text='Username' , border_color='#00ff00' )
username.place(x=58,y=110)

password = customtkinter.CTkEntry(master=frame , width=220 , placeholder_text='Password' , border_color='#00ff00')
password.place(x=58 , y=160)

gender = customtkinter.CTkComboBox(master=frame ,text_color='white',values=['Man','Woman'] , width=80 , height=25 ,button_color='#00ff00' ,border_color='#00ff00')
gender.place(x=198 , y= 210)

age = customtkinter.CTkEntry(master=frame , width=100 , placeholder_text='age' , border_color='#00ff00' ,height=25)
age.place(x=58 , y=210 )


btn_login = customtkinter.CTkButton(master=frame , width=110 , text="login" ,text_color='white',hover_color='#009e00' , fg_color='#00ff00',command=button_Login_function_usage)
btn_login.place(x=118 , y= 330)

check_robot = customtkinter.CTkCheckBox(master=frame , text='IM Not Robot', font=('Arial',20),checkbox_width=20 ,checkbox_height=20)
check_robot.place(x=95,y=270)

lable_singUP = customtkinter.CTkLabel(master=frame , text="")


page_1.mainloop()



