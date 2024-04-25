import colorama
from colorama import Fore, Back, Style
import random
import os
import smtplib
import mime-utils
from mime-utils import*
from email.mime.multipart import*
from email.mime.text import*

#colours
R=Fore.RED
G=Fore.GREEN
B=Fore.BLUE
Y=Fore.YELLOW
C=Fore.CYAN
M=Fore.MAGENTA
W=Fore.WHITE
#Style
BR=Style.BRIGHT
DR=Style.DIM

# Verification code
code = random.randint(100000, 999999)

# Email configurations
sender_email = "pythonterminal4@gmail.com"
sender_password = "02116kkk"

def send_code():
  receiver_email = str(input(B+BR+ "Enter the email address for verification code: "))
  message = MIMEMultipart()
  message['From'] = sender_email
  message['To'] = receiver_email
  message['Subject'] = "Verification Code"
  body = "Your verification code is " + str(code)
  message.attach(MIMEText(body, 'plain'))

  # Connect to SMTP server
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(sender_email,sender_password)

  # Send email
  server.send_message(message)

  # Quit the server
  server.quit()

def read_txt():
  with open("passwd.txt","r") as read_file:
    passwd = read_file.read().strip()
  return passwd

def verify(new,passwd):
  user_code = input(Y+BR+"Enter the verification code: ")
  if user_code == str(code):
    print(G+BR+"Verification successful!")
    new_pass(new,passwd)
    enter_pass(passwd)
    return True
  else:
    print(R+BR+"Verification failed. Please try again Later.")
    return False

def new_pass(new,passwd):
  
  write_txt(new)

def write_txt(new):
  with open("passwd.txt", "w") as write_file:
    write_file.write(new)
    print(G+BR+"Password updated successfully!")

def enter_pass(passwd):
  userpass = input(B+BR+"Enter your password: ")
  while userpass != passwd:
    print(R+BR+"Wrong password! Try again.")
    forget = input(C+BR+"Forget your password? (y/n): ")
    if forget.lower() == "y":
      send_code()
      try:
         verify(new,passwd)
      except :
        print(R+BR+"Verification failed. Please try again later.")
    else:
      userpass = input(M+BR+"Enter your password: ")
  print(G+BR+"Unlocked Successfully")

def main(new):
  passwd = read_txt()
  if not passwd:
    new_pass(new,passwd)
    exit()
  else:
    enter_pass(passwd)

passwd = read_txt()
if not passwd:
   new = input(B+BR+"Enter the new password: ")
   main(new)
else:
   enter_pass(passwd)
