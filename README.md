# Pyterminal-passwd
Pyterminal-passwd is one of the terminal password tool 

# Installation 
you must install all python module in latest version 

pip install -r requirements.txt
git clone https://github.com/Karthi02116K/Pyterminal-passwd.git

# Set up Terminal
if you using any shell type
"exit"for exit from shell
now you can see "$" symbol it is the default 

# now copy and paste this code
# ______________________________
cd && echo "if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
         command_not_found_handle() {
                 /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
         }
 fi

 PS1='$'
clear && cd Pyterminal-passwd && python pyterminal.py" > /data/data/com.termux/files/usr/etc/bash.bashrc && exit
# ______________________________
# Solution for Error 
1.install necessary pip modules
2.apt update && apt upgrade
3.if you see any error comment or take a screenshot and send to me 
