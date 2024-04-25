clear
cd $HOME

pkg install fish neofetch -y && cd && echo "if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
         command_not_found_handle() {
                 /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
         }
 fi

 PS1='$'
clear && neofetch && fish && cd Pyterminal-passwd && python pyterminal.py && cd $HOME" > /data/data/com.termux/files/usr/etc/bash.bashrc && exit